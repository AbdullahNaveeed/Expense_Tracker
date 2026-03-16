from expenses import (
    load_expenses,
    save_expenses,
    add_expense,
    display_all,
    get_category_total,
    get_monthly_summary,
    delete_expense,
    filter_by_month,
    get_most_expensive
)


def print_menu():
    print("\n==========================")
    print("  Personal Expense Tracker")
    print("==========================")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. View monthly summary")
    print("5. Exit")
    print("6. Delete expense")
    print("7. Filter expenses by month")
    print("8. Show most expensive expense")


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


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Input cannot be empty.")
        else:
            return value


def main():

    filename = "data.csv"

    # Load expenses on startup
    expenses = load_expenses(filename)

    while True:

        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":

            name = get_non_empty_input("Enter name: ")
            category = get_non_empty_input("Enter category: ")
            amount = get_valid_amount()

            add_expense(expenses, name, amount, category)

            save_expenses(expenses, filename)

            print("✅ Expense added successfully.")

        elif choice == "2":

            display_all(expenses)

        elif choice == "3":

            category = get_non_empty_input("Enter category: ")

            total = get_category_total(expenses, category)

            print(f"Total for {category}: £{total:.2f}")

        elif choice == "4":

            summary = get_monthly_summary(expenses)

            if not summary:
                print("No expenses recorded.")
            else:
                print("\nMonthly Summary:")
                for month, total in summary.items():
                    print(f"{month}: £{total:.2f}")

        elif choice == "5":

            print("Goodbye!")
            break
        elif choice == "6":
            name = input("Enter expense name to delete: ").strip()
            deleted = delete_expense(expenses, name)
            if deleted:
                save_expenses(expenses, filename)
                print("Expense deleted.")
            else:
                print("Expense not found.")
        elif choice == "7":
            month = input("Enter month (YYYY-MM): ").strip()
            filtered = filter_by_month(expenses, month)
            if not filtered:
                print("No expenses found for that month.")
            else:
                display_all(filtered)

        elif choice == "8":
            expense = get_most_expensive(expenses)
            if not expense:
                print("No expenses recorded.")
            else:
                print("\nMost Expensive Expense:")
                print(f"Name: {expense['name']}")
                print(f"Amount: £{expense['amount']:.2f}")
                print(f"Category: {expense['category']}")
                print(f"Date: {expense['date']}")
                
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()