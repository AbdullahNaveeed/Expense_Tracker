import csv
from models.expenses import Expense

class CSVStorage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        expenses = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expenses.append(Expense.from_dict(row))
        except FileNotFoundError:
            pass
        return expenses

    def save(self, expenses):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["name", "amount", "category", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())