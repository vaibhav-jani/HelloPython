# Hello Python

A Python project managed with Poetry.

## Installation

```bash
poetry install
```

## Development

This project uses:
- pytest for testing
- black for code formatting
- isort for import sorting
- flake8 for linting

To run tests:
```bash
poetry run pytest
```

To format code:
```bash
poetry run black .
poetry run isort .
```

To check code quality:
```bash
poetry run flake8
``` 