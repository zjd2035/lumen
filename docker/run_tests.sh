#!/bin/bash

set -e

printf "\nrunning black...\n"
black -l 120 --quiet lumen
black -l 120 --quiet tests

printf "\nrunning flake8...\n"
flake8

printf "\nrunning mypy...\n"
mypy lumen --ignore-missing-imports

printf "\nrunning tests...\n"
pytest tests
