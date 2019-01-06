#!/bin/sh

export PIPENV_VENV_IN_PROJECT="Y"

pipenv shell

pipenv install -e .