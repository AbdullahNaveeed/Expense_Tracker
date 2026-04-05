class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = amount
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.name} | {self.amount:.2f} | {self.category} | {self.date}"

    @classmethod
    def from_dict(cls, row):
        return cls(
            name=row["name"],
            amount=float(row["amount"]),
            category=row["category"],
            date=row["date"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }