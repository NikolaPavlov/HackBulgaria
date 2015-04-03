class BankAcc:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = int(balance)
        self.currency = currency

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError

        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError

        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer_to_acc(self, account, amount):
        if amount < 0:
            raise ValueError

        if account.currency != self.currency:
            raise ValueError

        if isinstance(account, BankAcc):
            if account.currency == self.currency:
                if amount > 0 and self.balance >= amount:
                    self.balance -= amount
                    account.balance += amount

    def __str__(self):
        strOutput = "Bank account for {} with balance of {}{}"
        return strOutput.format(self.name, self.balance, self.currency)

    def __int__(self):
        return int(self.balance)




if __name__ == "__main__":
    acc = BankAcc("Pepa", 111, '$$$')
    acc.deposit_money(222)
    print(acc.get_balance())
    print(str(acc))