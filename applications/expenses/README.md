# Expense Manager

A command-line application for managing personal expenses.

## Features

- Add new expenses with name and price
- Update existing expenses
- Delete expenses
- List all expenses with total
- Search expenses by name
- Persistent storage using JSON

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository
2. Navigate to the expense manager directory:
   ```bash
   cd applications/expenses
   ```

## Usage

Run the application:
```bash
python src/expense_manager.py
```

### Available Commands

1. **Add Expense**
   - Enter expense name
   - Enter price

2. **Update Expense**
   - Select expense by index
   - Enter new name (optional)
   - Enter new price (optional)

3. **Delete Expense**
   - Select expense by index

4. **List Expenses**
   - Shows all expenses with total

5. **Search Expenses**
   - Enter search term
   - Shows matching expenses with total

6. **Exit**
   - Closes the application

## Data Storage

Expenses are stored in `expenses.json` in the same directory as the script. 