# Expense Management API

A simple expense management system with a REST API server and command-line client.

## Project Structure

```
expenses_api/
├── src/
│   ├── client/           # Client package
│   │   ├── __init__.py
│   │   └── client.py     # Command-line client implementation
│   ├── server/          # Server package
│   │   ├── __init__.py
│   │   └── server.py    # Flask server implementation
│   ├── models/          # Shared models package
│   │   ├── __init__.py
│   │   └── expense.py   # Expense data model
│   ├── main.py         # Main entry point
│   └── expenses.json   # Data storage
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Features

- Add, update, delete, and list expenses
- Search expenses by name
- Persistent storage using JSON file
- RESTful API with Flask
- Command-line client interface

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Server

From the `expenses_api` directory:
```bash
python -m src.server.server
```

The server will start on http://localhost:5000

### Run the Client

In a new terminal, from the `expenses_api` directory:
```bash
python -m src.client.client
```

### Using the Main Script

You can also use the main script to run both server and client:
```bash
python -m main
```

## API Endpoints

- `GET /api/expenses` - List all expenses
- `POST /api/expenses` - Add a new expense
- `PUT /api/expenses/<index>` - Update an expense
- `DELETE /api/expenses/<index>` - Delete an expense
- `GET /api/expenses/search?q=<query>` - Search expenses by name

## Data Model

```python
@dataclass
class Expense:
    name: str
    price: float
```

## Dependencies

- Flask 3.0.2
- Requests 2.31.0 