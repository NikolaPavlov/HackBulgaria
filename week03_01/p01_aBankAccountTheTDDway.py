class BankAcc:
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = int(balance)
        self.currency = currency

    def deposit_money(self, money):
        if money < 0:
            raise ValueError

        self.balance += money


    def balance(self):
        return self.balance


if __name__ == "__main__":
    acc = BankAcc("account", 111, '$$$')
    acc.deposit_money(222)
    print(acc.balance())
