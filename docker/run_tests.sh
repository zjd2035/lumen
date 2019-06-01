#!/bin/bash

echo "running black..."
black -l 120 lumen
black -l 120 tests

echo "running flake8..."
flake8

echo "running tests"
pytest tests
