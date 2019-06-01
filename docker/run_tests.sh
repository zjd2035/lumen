#!/bin/bash

echo "running black..."
black -l 120 lumen
black -l 120 tests

echo "running tests"
pytest tests
