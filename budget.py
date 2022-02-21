class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        # self.balance = 0.0

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # amount = 0
        # description = ""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_amount = 0
        for item in self.ledger:
            total_amount += item['amount']

        return total_amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to", category.name)
            category.deposit(amount, "Transfer to", self.name)
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False


def create_spend_chart(categories):
        pass
