const path = require("path");
const webpack = require("webpack");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");
const sass = require("sass");

const pkg = require("./package.json");

// Some libraries import Node modules but don't use them in the browser.
// Tell Webpack to provide empty mocks for them so importing them works.
const node = {
  dgram: "empty",
  fs: "empty",
  net: "empty",
  tls: "empty",
  child_process: "empty",
};

// https://webpack.js.org/configuration/stats/
const stats = {
  // Tells stats whether to add the build date and the build time information.
  builtAt: false,
  // Add chunk information (setting this to `false` allows for a less verbose output)
  chunks: false,
  // Add the hash of the compilation
  hash: false,
  // `webpack --colors` equivalent
  colors: true,
  // Add information about the reasons why modules are included
  reasons: false,
  // Add webpack version information
  version: false,
  // Add built modules information
  modules: false,
  // Show performance hint when file size exceeds `performance.maxAssetSize`
  performance: false,
  // Add children information
  children: false,
  // Add asset Information.
  assets: false,
};

/**
 * Base Webpack config, defining how our code should compile.
 */
const webpackConfig = (environment) => {
  const isProduction = environment === "production";

  const plugins = [
    new webpack.NoEmitOnErrorsPlugin(),
    new MiniCssExtractPlugin({
      filename: "[name].css",
    }),
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify(environment),
      PKG_VERSION: JSON.stringify(pkg.version),
    }),

    isProduction
      ? new webpack.ExtendedAPIPlugin()
      : new webpack.HotModuleReplacementPlugin(),
  ];

  if (isProduction) {
    plugins.push(
      new BundleAnalyzerPlugin({
        // Can be `server`, `static` or `disabled`.
        analyzerMode: "static",
        // Path to bundle report file that will be generated in `static` mode.
        reportFilename: path.join(__dirname, "webpack-stats.html"),
        // Automatically open report in default browser
        openAnalyzer: false,
        logLevel: "info",
      }),
    );
  }

  const compiler = {
    mode: isProduction ? "production" : "development",

    // See https://webpack.js.org/configuration/devtool/.
    devtool: isProduction ? "none" : "cheap-module-source-map",

    entry: {
      draftail: "./draftail/draftail.entry.js",
    },
    output: {
      path: path.join(__dirname, "draftail", "static"),
      filename: "[name].bundle.js",
      publicPath: "/static/",
    },
    plugins,
    module: {
      rules: [
        {
          test: /\.js$/,
          use: ["babel-loader"],
          exclude: /node_modules/,
        },

        {
          test: /\.(scss|css)$/,
          use: [
            isProduction ? MiniCssExtractPlugin.loader : "style-loader",
            {
              loader: "css-loader",
              options: {
                sourceMap: !isProduction,
              },
            },
            {
              loader: "postcss-loader",
              options: {
                sourceMap: !isProduction,
                plugins: () => [
                  autoprefixer(),
                  cssnano({
                    preset: "default",
                  }),
                ],
              },
            },
            {
              loader: "sass-loader",
              options: {
                sourceMap: !isProduction,
                implementation: sass,
              },
            },
          ],
        },
      ],
    },

    optimization: {
      minimize: isProduction,
      minimizer: [
        new TerserPlugin({
          // See https://github.com/facebook/create-react-app/blob/78fb4cf11461107a485a0b1378e809b9684d1f22/packages/react-scripts/config/webpack.config.js#L210.
          terserOptions: {
            parse: {
              // We want terser to parse ecma 8 code. However, we don't want it
              // to apply any minification steps that turns valid ecma 5 code
              // into invalid ecma 5 code. This is why the 'compress' and 'output'
              // sections only apply transformations that are ecma 5 safe
              // https://github.com/facebook/create-react-app/pull/4234
              ecma: 8,
            },
            compress: {
              ecma: 5,
              warnings: false,
              // Disabled because of an issue with Uglify breaking seemingly valid code:
              // https://github.com/facebook/create-react-app/issues/2376
              // Pending further investigation:
              // https://github.com/mishoo/UglifyJS2/issues/2011
              comparisons: false,
              // Disabled because of an issue with Terser breaking valid code:
              // https://github.com/facebook/create-react-app/issues/5250
              // Pending further investigation:
              // https://github.com/terser-js/terser/issues/120
              inline: 2,
            },
            mangle: {
              safari10: true,
            },
            output: {
              ecma: 5,
              comments: false,
              // Turned on because emoji and regex is not minified properly using default
              // https://github.com/facebook/create-react-app/issues/2488
              ascii_only: true,
            },
          },
          // Note: this does not work on WSL.
          parallel: true,
          // Enable file caching
          // cache: true,
        }),
      ],
    },

    // Turn off performance hints during development because we don't do any
    // splitting or minification in interest of speed. These warnings become
    // cumbersome.
    performance: {
      hints: isProduction && "warning",
    },

    stats,

    node,

    // https://webpack.js.org/configuration/dev-server/#devserver
    devServer: {
      // contentBase: path.join(__dirname, "public"),
      // watchContentBase: true,
      compress: true,
      hot: true,
      overlay: true,
      clientLogLevel: "none",
      stats,
      disableHostCheck: true,
      port: 3000,
      index: "",
      proxy: {
        context: () => true,
        target: "http://localhost:8000",
      },
    },
  };

  return compiler;
};

module.exports = webpackConfig;
