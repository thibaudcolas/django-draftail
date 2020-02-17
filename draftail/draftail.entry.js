import React from "react";
import ReactDOM from "react-dom";
import { DraftailEditor } from "draftail";

import "./draftail.entry.scss";

// See https://stackoverflow.com/a/4793630/1798491.
const insertAfter = (newNode, referenceNode) => {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
};

const fields = [...document.querySelectorAll("[data-django-draftail]")];

fields.forEach((field) => {
  const editor = <DraftailEditor inlineStyles={[{ type: "BOLD" }]} />;
  const mount = document.createElement("div");
  mount.setAttribute("data-django-draftail-wrapper", true);
  insertAfter(mount, field);
  ReactDOM.render(editor, mount);
});
