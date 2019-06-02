#!/bin/bash

printf "\nrunning black..."
black -l 120 --quiet lumen
black -l 120 --quiet tests

printf "\n\nrunning flake8..."
flake8

printf "\n\nrunning mypy..."
mypy lumen --ignore-missing-imports

printf "\n\nrunning tests...\n"
pytest tests
