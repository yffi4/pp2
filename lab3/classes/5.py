class Account():
    owner = ""
    balance = 0

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} was withdrew from your account. Your balance equal to {self.balance}")
        else:
            print("You don't have enough money on your account")


x = Account()
x.deposit(100)
x.withdraw(340)
x.withdraw(15)

