from datetime import datetime
from models.expenses import Expense

class ExpenseManager:
    def __init__(self, storage):
        self.storage = storage
        self.expenses = self.storage.load()

    
    def add_expense(self, name, amount, category):
        date = datetime.now().strftime("%Y-%m-%d")
        expense = Expense(name, amount, category, date)
        self.expenses.append(expense)
        self.storage.save(self.expenses)

    def get_all(self):
        return self.expenses

    def get_total(self):
        return sum(e.amount for e in self.expenses)

    def get_by_category(self, category):
        return [e for e in self.expenses if e.category == category]

    def get_monthly_summary(self):
        summary = {}
        for e in self.expenses:
            summary.setdefault(e.date, 0)
            summary[e.date] += e.amount
        return summary