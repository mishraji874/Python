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
        self.score = 0

    def add_transaction(self, amount):
        self.transactions.append(amount)

    def calculate_score(self):
        pass

class SavingAccount(Customer):
    def calculate_score(self):
        credit_score = 0
        debit_score = 0
        balance_score = 0
        total_credit = sum([t for t in self.transactions if t > 0])
        total_debit = abs(sum([t for t in self.transactions if t < 0]))
        credit_score = total_credit // 2000
        debit_score = total_debit // 2000
        balance_score = 1 if sum(self.transactions) >= 10000 else 0
        self.score = credit_score - (debit_score * 0.25) + balance_score
        return self.score

class CurrentAccount(Customer):
    def calculate_score(self):
        credit_score = 0
        balance_score = 0
        overdue_score = 0
        total_credit = sum([t for t in self.transactions if t > 0])
        credit_score = total_credit // 2000
        balance_score = 1 if sum(self.transactions) >= 10000 else 0
        overdue_balance = max(0, sum(self.transactions) - 25000)
        overdue_score = -overdue_balance // 2500
        self.score = credit_score + balance_score + overdue_score
        return self.score

class LoanAccount(Customer):
    def calculate_score(self):
        loan_repayment_score = 0
        penalty_score = 0
        for t in self.transactions:
            if t > 0:
                loan_repayment_score += 1
            elif t < 0:
                penalty_score -= 0.5
        self.score = loan_repayment_score + penalty_score
        return self.score

customer = SavingAccount("John Doe", "123 Main St", "Saving", 123456)
customer.add_transaction(2000)
customer.add_transaction(-500)
customer.add_transaction(8000)
score = customer.calculate_score()
print(f"Score: {score}")