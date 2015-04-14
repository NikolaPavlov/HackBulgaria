class Bill:

    def __init__(self, num):
        # negative bill check
        if num <= 0:
            raise ValueError

        # floating bill check
        if not isinstance(num, int):
            raise ValueError

        self.num = num
        self.money_holder = {}

    def __str__(self):
        return("A " + str(self.num) + "$ bill")

    def __repr__(self):
        return(str(self))

    def __int__(self):
        return(int(self.num))

    def __eq__(self, other):
        return self.num == other.num

    def __hash__(self):
        return hash(self.num.__hash__())

##################################################


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum([int(bill) for bill in self.bills])

    # iterate obj
    def __getitem__(self, index):
        return self.bills[index]

##################################################


class CashDesk:

    def __init__(self):
        self.bank = {}
        self.all_money = 0

    def add_in_bank(self, money):
        if isinstance(money, Bill):
            if money in self.bank:
                self.bank[money] += 1
            else:
                self.bank[money] = 1
        elif isinstance(money, BatchBill):
            for bill in money:
                if bill in self.bank:
                    self.bank[bill] += 1
                else:
                    self.bank[bill] = 1

    def take_money(self, money):
        self.add_in_bank(money)

        if isinstance(money, Bill):
            self.all_money += int(money)
        elif isinstance(money, BatchBill):
            self.all_money += money.total()

    def total(self):
        return self.all_money

    def inspect(self):
        return self.bank

##################################################
