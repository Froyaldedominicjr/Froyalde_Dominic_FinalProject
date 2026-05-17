"""Budget manager module."""

import json
import os
from manager import BudgetManager

class BudgetManager:
    """Handles transaction operations."""

    def __init__(self):
        """Initialize transaction list and file name."""
        self.transactions = []
        self.file = "data.json"

    def add_transaction(self, t_type):
        """Add a new transaction."""
        category = input("Category: ")
        amount = float(input("Amount: "))
        date = input("Date (YYYY-MM-DD): ")

        transaction = Transaction(t_type, category, amount, date)
        self.transactions.append(transaction)

        print("Transaction added.")

    def view_transactions(self):
        """Display all transactions."""
        if not self.transactions:
            print("No transactions found.")
            return

        for t in self.transactions:
            print(f"{t.date} | {t.t_type} | {t.category} | {t.amount}")

    def monthly_summary(self):
        """Display income, expense, and balance summary."""
        income = sum(t.amount for t in self.transactions if t.t_type == "Income")
        expense = sum(t.amount for t in self.transactions if t.t_type == "Expense")

        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Balance: {income - expense}")

    def search_transaction(self):
        """Search transactions by category."""
        keyword = input("Enter category: ")

        results = [
            t for t in self.transactions
            if keyword.lower() in t.category.lower()
        ]

        if results:
            for t in results:
                print(f"{t.date} | {t.t_type} | {t.category} | {t.amount}")
        else:
            print("No matching transactions.")

    def save_data(self):
        """Save transactions to JSON file."""
        with open(self.file, "w") as f:
            json.dump([t.to_dict() for t in self.transactions], f, indent=4)

    def load_data(self):
        """Load transactions from JSON file."""
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                data = json.load(f)

                for item in data:
                    self.transactions.append(
                        Transaction(
                            item["type"],
                            item["category"],
                            item["amount"],
                            item["date"]
                        )
                    )