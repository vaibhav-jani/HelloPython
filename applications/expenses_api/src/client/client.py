import requests
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import json
from pathlib import Path
from datetime import datetime
from ..models import Expense


class ExpenseClient:
    def __init__(self, base_url: str = " http://127.0.0.1:5000"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and raise exceptions for errors."""
        response.raise_for_status()
        return response.json()

    def get_expenses(self) -> List[Expense]:
        """Get all expenses."""
        response = self.session.get(f"{self.base_url}/api/expenses")
        data = self._handle_response(response)
        return [Expense(**item) for item in data]

    def add_expense(self, name: str, price: float) -> Expense:
        """Add a new expense."""
        data = {"name": name, "price": price}
        response = self.session.post(
            f"{self.base_url}/api/expenses",
            json=data
        )
        data = self._handle_response(response)
        return Expense(**data)

    def update_expense(self, index: int, name: Optional[str] = None, price: Optional[float] = None) -> Expense:
        """Update an existing expense."""
        data = {}
        if name is not None:
            data['name'] = name
        if price is not None:
            data['price'] = price

        response = self.session.put(
            f"{self.base_url}/api/expenses/{index}",
            json=data
        )
        data = self._handle_response(response)
        return Expense(**data)

    def delete_expense(self, index: int) -> Expense:
        """Delete an expense."""
        response = self.session.delete(f"{self.base_url}/api/expenses/{index}")
        data = self._handle_response(response)
        return Expense(**data)

    def search_expenses(self, query: str) -> List[Expense]:
        """Search expenses by name."""
        response = self.session.get(
            f"{self.base_url}/api/expenses/search",
            params={"q": query}
        )
        data = self._handle_response(response)
        return [Expense(**item) for item in data]


def main():
    client = ExpenseClient()

    while True:
        print("\nExpense Manager (REST Client)")
        print("=" * 40)
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. List Expenses")
        print("5. Search Expenses")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        try:
            if choice == "1":
                name = input("Enter expense name: ")
                try:
                    price = float(input("Enter price: $"))
                    expense = client.add_expense(name, price)
                    print(
                        f"Added expense: {expense.name} - ${expense.price:.2f}")
                except ValueError:
                    print("Invalid price! Please enter a number.")

            elif choice == "2":
                expenses = client.get_expenses()
                if not expenses:
                    print("No expenses found!")
                    continue

                print("\nExpense List:")
                print("-" * 40)
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.name} - ${expense.price:.2f}")

                try:
                    index = int(
                        input("\nEnter index to update (1-{}): ".format(len(expenses)))) - 1
                    name = input(
                        "Enter new name (press Enter to skip): ").strip()
                    price_str = input(
                        "Enter new price (press Enter to skip): ").strip()

                    data = {}
                    if name:
                        data['name'] = name
                    if price_str:
                        data['price'] = float(price_str)

                    expense = client.update_expense(index, **data)
                    print(
                        f"Updated expense: {expense.name} - ${expense.price:.2f}")
                except ValueError:
                    print("Invalid input!")

            elif choice == "3":
                expenses = client.get_expenses()
                if not expenses:
                    print("No expenses found!")
                    continue

                print("\nExpense List:")
                print("-" * 40)
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.name} - ${expense.price:.2f}")

                try:
                    index = int(
                        input("\nEnter index to delete (1-{}): ".format(len(expenses)))) - 1
                    expense = client.delete_expense(index)
                    print(
                        f"Deleted expense: {expense.name} - ${expense.price:.2f}")
                except ValueError:
                    print("Invalid index!")

            elif choice == "4":
                expenses = client.get_expenses()
                if not expenses:
                    print("No expenses found!")
                    continue

                print("\nExpense List:")
                print("-" * 40)
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.name} - ${expense.price:.2f}")

                total = sum(expense.price for expense in expenses)
                print("-" * 40)
                print(f"Total: ${total:.2f}")

            elif choice == "5":
                query = input("Enter search term: ")
                expenses = client.search_expenses(query)
                if not expenses:
                    print(f"No expenses found matching '{query}'")
                    continue

                print(f"\nExpenses matching '{query}':")
                print("-" * 40)
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense.name} - ${expense.price:.2f}")

                total = sum(expense.price for expense in expenses)
                print("-" * 40)
                print(f"Total: ${total:.2f}")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {e}")
            print("Make sure the server is running on http://localhost:5000")


if __name__ == "__main__":
    main()
