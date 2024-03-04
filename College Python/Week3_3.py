class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Customer(Bank):
    def __init__(self, name, address, account_type, account_number):
        super().__init__(name, address)
        self.account_type = account_type
        self.account_number = account_number
        self.transactions = []

    def add_transaction(self, amount):
        self.transactions.append(amount)

class SavingAccount(Customer):
    pass

class LoanAccount(Customer):
    pass

class CurrentAccount(Customer):
    pass

customer = SavingAccount("John Doe", "123 Main St", "Saving", 123456)
customer.add_transaction(1000)
customer.add_transaction(-500)
print(customer.transactions)