class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")


def account_balance() -> float:
    account = BankAccount("Dana", 100.0)
    account.deposit(50.0)
    account.withdraw(30.0)
    return account.balance

result = account_balance()
