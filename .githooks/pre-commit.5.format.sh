#!/usr/bin/env bash
# Format and re-stage fully staged files only.

if [ -n "$PRETTIER_FULLY_STAGED" ];
then
  npx prettier --write $PRETTIER_FULLY_STAGED
  git add $PRETTIER_FULLY_STAGED
fi

if [ -n "$PRETTIER_STAGED" ];
then
  npx prettier --check $PRETTIER_STAGED
fi

if [ -n "$PY_FULLY_STAGED" ];
then
  isort $PY_FULLY_STAGED
  black $PY_FULLY_STAGED
  git add $PY_FULLY_STAGED
fi

if [ -n "$PY_STAGED" ];
then
  isort --check-only --diff $PY_STAGED
  black --check $PY_STAGED
fi
