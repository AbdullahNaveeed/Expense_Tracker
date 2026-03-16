import csv
from datetime import datetime


def load_expenses(filename):
    expenses = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = {
                    "name": row["name"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                }

                expenses.append(expense)

    except FileNotFoundError:
        # If the file doesn't exist yet, return empty list
        pass

    return expenses


def save_expenses(expenses, filename):

    with open(filename, "w", newline="") as file:

        fieldnames = ["name", "amount", "category", "date"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)


def add_expense(expenses, name, amount, category):

    date = datetime.now().strftime("%Y-%m")

    expense = {
        "name": name.lower(),
        "amount": amount,
        "category": category.lower(),
        "date": date
    }

    expenses.append(expense)


def display_all(expenses):

    if not expenses:
        print("No expenses recorded.")
        return

    print("\n---------------------------------------------")
    print(f"{'Name':<15}{'Amount':<10}{'Category':<15}{'Date'}")
    print("---------------------------------------------")

    for expense in expenses:
        print(
            f"{expense['name']:<15}"
            f"{expense['amount']:<10.2f}"
            f"{expense['category']:<15}"
            f"{expense['date']}"
        )


def get_category_total(expenses, category):

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    return total


def get_monthly_summary(expenses):

    summary = {}

    for expense in expenses:

        month = expense["date"]

        if month not in summary:
            summary[month] = 0

        summary[month] += expense["amount"]

    return summary

def delete_expense(expenses, name):

    for expense in expenses:
        if expense["name"].lower() == name.lower():
            expenses.remove(expense)
            return True

    return False

def filter_by_month(expenses, month):

    filtered = []

    for expense in expenses:
        if expense["date"] == month:
            filtered.append(expense)

    return filtered

def get_most_expensive(expenses):

    if not expenses:
        return None

    return max(expenses, key=lambda e: e["amount"])