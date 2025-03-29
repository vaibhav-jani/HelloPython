# Expense Manager API

A RESTful API application demonstrating how to build and consume web services in Python.

## Features

- RESTful API server using Flask
- REST client using requests library
- CRUD operations for expenses
- Search functionality
- Persistent storage using JSON
- Error handling and validation

## Requirements

- Python 3.6 or higher
- Flask
- requests

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask requests
   ```

## Usage

### Starting the Server

1. Navigate to the API directory:
   ```bash
   cd applications/expense_api
   ```

2. Start the server:
   ```bash
   python src/mock_server.py
   ```
   The server will run on http://localhost:5000

### Using the Client

1. In a new terminal, navigate to the API directory:
   ```bash
   cd applications/expense_api
   ```

2. Run the client:
   ```bash
   python src/expense_client.py
   ```

## API Endpoints

- `GET /api/expenses` - List all expenses
- `POST /api/expenses` - Add a new expense
- `PUT /api/expenses/<index>` - Update an expense
- `DELETE /api/expenses/<index>` - Delete an expense
- `GET /api/expenses/search?q=<query>` - Search expenses by name

## Example API Usage

```python
# Using curl
# List expenses
curl http://localhost:5000/api/expenses

# Add expense
curl -X POST http://localhost:5000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"name": "Groceries", "price": 50.25}'

# Update expense
curl -X PUT http://localhost:5000/api/expenses/0 \
  -H "Content-Type: application/json" \
  -d '{"price": 55.00}'

# Delete expense
curl -X DELETE http://localhost:5000/api/expenses/0

# Search expenses
curl http://localhost:5000/api/expenses/search?q=groceries
```

## Data Storage

Expenses are stored in `expenses.json` in the `applications/expense_api` directory. 