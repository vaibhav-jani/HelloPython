from flask import Flask, request, jsonify
from typing import List
import json
from pathlib import Path
from ..models import Expense

app = Flask(__name__)


class ExpenseStore:
    def __init__(self):
        self.expenses: List[Expense] = []
        self.load_expenses()

    def load_expenses(self):
        file_path = Path(__file__).parent.parent / "expenses.json"
        if file_path.exists():
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    self.expenses = [Expense(**item) for item in data]
            except Exception as e:
                print(f"Error loading expenses: {e}")
                self.expenses = []

    def save_expenses(self):
        file_path = Path(__file__).parent.parent / "expenses.json"
        try:
            with open(file_path, 'w') as f:
                json.dump([vars(expense)
                          for expense in self.expenses], f, indent=2)
        except Exception as e:
            print(f"Error saving expenses: {e}")


store = ExpenseStore()


@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    """Get all expenses."""
    return jsonify([vars(expense) for expense in store.expenses])


@app.route('/api/expenses', methods=['POST'])
def add_expense():
    """Add a new expense."""
    data = request.get_json()
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        expense = Expense(name=data['name'], price=float(data['price']))
        store.expenses.append(expense)
        store.save_expenses()
        return jsonify(vars(expense)), 201
    except ValueError:
        return jsonify({'error': 'Invalid price'}), 400


@app.route('/api/expenses/<int:index>', methods=['PUT'])
def update_expense(index):
    """Update an existing expense."""
    if index < 0 or index >= len(store.expenses):
        return jsonify({'error': 'Invalid index'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    expense = store.expenses[index]
    if 'name' in data:
        expense.name = data['name']
    if 'price' in data:
        try:
            expense.price = float(data['price'])
        except ValueError:
            return jsonify({'error': 'Invalid price'}), 400

    store.save_expenses()
    return jsonify(vars(expense))


@app.route('/api/expenses/<int:index>', methods=['DELETE'])
def delete_expense(index):
    """Delete an expense."""
    if index < 0 or index >= len(store.expenses):
        return jsonify({'error': 'Invalid index'}), 404

    expense = store.expenses.pop(index)
    store.save_expenses()
    return jsonify(vars(expense))


@app.route('/api/expenses/search', methods=['GET'])
def search_expenses():
    """Search expenses by name."""
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])

    matching_expenses = [
        expense for expense in store.expenses
        if query in expense.name.lower()
    ]
    return jsonify([vars(expense) for expense in matching_expenses])


def main():
    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
