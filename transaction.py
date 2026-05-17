## transaction.py

python
"""Transaction model."""

class Transaction:
    """Represents a financial transaction."""

    def __init__(self, t_type, category, amount, date):
        self.t_type = t_type
        self.category = category
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "type": self.t_type,
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
        }
```

