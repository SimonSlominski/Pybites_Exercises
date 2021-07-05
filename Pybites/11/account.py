"""
Bite 11. Enrich a class with dunder methods

Let's enrich an Account class by adding dunder (aka special) methods to support the following:
1) length of the object: len(acc) returns the number of transactions
2) account comparison: acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
3) indexing: acc[n] shows the nth transaction onaccount (0 based)
4) iteration: list(acc) returns a sequence of account transactions
5) operator overloading: acc + int and acc - int can be used to add/subtract money
6) string representation: str(acc) returns NAME account - balance: INT
"""

class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __add__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use int for amount")
        return self._transactions.append(amount)

    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Please use int for amount")
        return self._transactions.append(amount * -1)

    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __getitem__(self, position):
        return self._transactions[position]

    def __str__(self):
        return f"{self.name.capitalize()} account - balance: {int(self.balance)}"
