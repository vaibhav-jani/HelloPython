#!/bin/bash

echo "Formatting Python code with Black..."
poetry run black .

echo "Sorting imports with isort..."
poetry run isort .

echo "Formatting complete!" 