from storage.csv_storage import CSVStorage
from managers.expense_manager import ExpenseManager
from models.category import Category


def print_menu():
    print("\n" + "=" * 50)
    print(f"{'Personal Expense Tracker':^50}")
    print("=" * 50)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. View monthly summary")
    print("5. Exit")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_category():
    print("\nSelect Category:")
    for i, category in enumerate(Category, start=1):
        print(f"{i}. {category.value}")

    while True:
        try:
            choice = int(input("Enter choice: "))
            return list(Category)[choice - 1].value
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")


def main():
    storage = CSVStorage("data.csv")
    manager = ExpenseManager(storage)

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue

            amount = get_valid_amount()
            category = get_category()

            manager.add_expense(name, amount, category)
            print("✅ Expense added successfully.")

        elif choice == "2":
            expenses = manager.get_all()
            if not expenses:
                print("No expenses recorded.")
                continue

            print("\n----------------------------------------------------------")
            print(f"{'Name':<15}{'Amount':<10}{'Category':<15}{'Date'}")
            print("----------------------------------------------------------")

            for e in expenses:
                print(
                    f"{e.name:<15}"
                    f"{e.amount:<10.2f}"
                    f"{e.category:<15}"
                    f"{e.date}"
                )

        elif choice == "3":
            category = get_category()
            expenses = manager.get_by_category(category)
            total = sum(e.amount for e in expenses)

            print(f"Total for {category}: £{total:.2f}")

        elif choice == "4":
            summary = manager.get_monthly_summary()
            if not summary:
                print("No expenses recorded.")
                continue

            print("\nMonthly Summary:")
            for month, total in summary.items():
                print(f"{month}: £{total:.2f}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()