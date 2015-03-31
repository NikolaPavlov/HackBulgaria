class Bill:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return("A " + str(self.num)+ "$ bill")

    #
    #def __repr__(self):
    #   return("This is repr" + str(self.num))

    def __int__(self):
        return(int(self.num))

    def __eq__(self, other):
        return self.num == other.num

    def __hash__(self):
        return hash(self.num)

##################################################

class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(bills)

    def total(self):
        total_sum = 0
        for bill in self.bills:
            total_sum += int(bill)

    # iterate obj
    def __getitem__(self, index):
        return self.bills[index]

##################################################

class CashDesk:
    def __init__(self):
        self.money = []

    def take_money(self, currency):
        self.money.append(currency)

    def total(self):
        result = []
        for money in self.money:
            # go implement int in previous 2 classes
            result += int(money)
        return result
