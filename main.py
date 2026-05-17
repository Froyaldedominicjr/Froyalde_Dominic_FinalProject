"""Main entry point for BudgetWise CLI."""

from manager import BudgetManager


def menu():
    """Display the main menu and handle user input."""
    manager = BudgetManager()
    manager.load_data()

    while True:
        print("\n=== BudgetWise CLI ===")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Monthly Summary")
        print("5. Search Transaction")
        print("6. Save and Exit")

        choice = input("Choose: ")

        if choice == "1":
            manager.add_transaction("Income")
        elif choice == "2":
            manager.add_transaction("Expense")
        elif choice == "3":
            manager.view_transactions()
        elif choice == "4":
            manager.monthly_summary()
        elif choice == "5":
            manager.search_transaction()
        elif choice == "6":
            manager.save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()