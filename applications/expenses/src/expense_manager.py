from dataclasses import dataclass
from typing import List, Optional
import json
from pathlib import Path


@dataclass
class Expense:
    name: str
    price: float


class ExpenseManager:
    def __init__(self):
        # Get the application root directory (applications/expenses)
        self.root_dir = Path(__file__).parent.parent
        self.file_path = self.root_dir / "expenses.json"
        self.expenses: List[Expense] = []
        self.load_expenses()

    def load_expenses(self) -> None:
        """Load expenses from JSON file."""
        if self.file_path.exists():
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    self.expenses = [Expense(**item) for item in data]
            except Exception as e:
                print(f"Error loading expenses: {e}")
                self.expenses = []

    def save_expenses(self) -> None:
        """Save expenses to JSON file."""
        try:
            with open(self.file_path, 'w') as f:
                json.dump([vars(expense)
                          for expense in self.expenses], f, indent=2)
        except Exception as e:
            print(f"Error saving expenses: {e}")

    def add_expense(self, name: str, price: float) -> None:
        """Add a new expense."""
        expense = Expense(name=name, price=price)
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added expense: {name} - ${price:.2f}")

    def update_expense(self, index: int, name: Optional[str] = None, price: Optional[float] = None) -> None:
        """Update an existing expense."""
        if 0 <= index < len(self.expenses):
            expense = self.expenses[index]
            if name is not None:
                expense.name = name
            if price is not None:
                expense.price = price
            self.save_expenses()
            print(f"Updated expense: {expense.name} - ${expense.price:.2f}")
        else:
            print("Invalid index!")

    def delete_expense(self, index: int) -> None:
        """Delete an expense by index."""
        if 0 <= index < len(self.expenses):
            expense = self.expenses.pop(index)
            self.save_expenses()
            print(f"Deleted expense: {expense.name} - ${expense.price:.2f}")
        else:
            print("Invalid index!")

    def list_expenses(self) -> None:
        """List all expenses with total."""
        if not self.expenses:
            print("No expenses found!")
            return

        print("\nExpense List:")
        print("-" * 40)
        for i, expense in enumerate(self.expenses):
            print(f"{i}. {expense.name} - ${expense.price:.2f}")

        total = sum(expense.price for expense in self.expenses)
        print("-" * 40)
        print(f"Total: ${total:.2f}")

    def search_expenses(self, query: str) -> None:
        """Search expenses by name."""
        query = query.lower()
        matching_expenses = [
            expense for expense in self.expenses
            if query in expense.name.lower()
        ]

        if not matching_expenses:
            print(f"No expenses found matching '{query}'")
            return

        print(f"\nExpenses matching '{query}':")
        print("-" * 40)
        for expense in matching_expenses:
            print(f"{expense.name} - ${expense.price:.2f}")

        total = sum(expense.price for expense in matching_expenses)
        print("-" * 40)
        print(f"Total: ${total:.2f}")


def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Manager")
        print("=" * 40)
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. List Expenses")
        print("5. Search Expenses")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            name = input("Enter expense name: ")
            try:
                price = float(input("Enter price: $"))
                manager.add_expense(name, price)
            except ValueError:
                print("Invalid price! Please enter a number.")

        elif choice == "2":
            manager.list_expenses()
            try:
                index = int(input("\nEnter index to update: "))
                name = input("Enter new name (press Enter to skip): ").strip()
                price_str = input(
                    "Enter new price (press Enter to skip): ").strip()

                price = float(price_str) if price_str else None
                name = name if name else None

                manager.update_expense(index, name, price)
            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            manager.list_expenses()
            try:
                index = int(input("\nEnter index to delete: "))
                manager.delete_expense(index)
            except ValueError:
                print("Invalid index!")

        elif choice == "4":
            manager.list_expenses()

        elif choice == "5":
            query = input("Enter search term: ")
            manager.search_expenses(query)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
