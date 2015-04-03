class BankAcc:

    def __init__(self, name, balance, currency):
        # TODO: add check for name, balance and currnecy
        # invalid input is possible!!!
        self.name = name
        self.balance = int(balance)
        self.currency = currency
        self.history = "Created ---> Name: {}, Balance: {}, Currency: {}".format(self.name, self.balance, self.currency) + '\r'

    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError

        self.balance += amount
        self.history += "Deposit: {}".format(amount) + '\r'

    def get_balance(self):
        self.history += "Balance checked: {}".format(self.balance) + '\r'
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError

        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.history += "Withdraw: {}".format(amount) + '\r'
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
                    self.history += "Transfer from: {} to: {} amount: {}".format(self.name, account.name, amount) + '\r'

    def get_history(self):
        self.history += "History checked" + '\r'
        return self.history

    def __str__(self):
        strOutput = "Bank account for {} with balance of {}{}"
        return strOutput.format(self.name, self.balance, self.currency)

    def __int__(self):
        return int(self.balance)



# Test History
if __name__ == "__main__":
    acc = BankAcc("Pepa", 111, '$$$')
    acc1 = BankAcc("Gogo", 100, '$$$')
    acc.deposit_money(222)
    acc.get_balance()
    acc.get_history()
    acc.withdraw(10)
    acc.transfer_to_acc(acc1, 10)
    acc.get_balance()
    print(acc.get_history())