class ITCalculator:
    def __init__(self, transactions):
        self.transactions = transactions
        self.saving_limit = 150000
        self.first_tier_limit = 100000
        self.second_tier_limit = 150000
        self.third_tier_limit = float('inf')
        self.first_tier_rate = 0.06
        self.second_tier_rate = 0.08
        self.third_tier_rate = 0.10

    def calculate_tax(self):
        total_amount = sum(self.transactions)
        saving_amount = min(total_amount, self.saving_limit)
        taxable_amount = total_amount - saving_amount
        if taxable_amount <= self.first_tier_limit:
            tax = taxable_amount * self.first_tier_rate
        elif taxable_amount <= self.second_tier_limit:
            tax = (self.first_tier_limit * self.first_tier_rate +
                   (taxable_amount - self.first_tier_limit) * self.second_tier_rate)
        else:
            tax = (self.first_tier_limit * self.first_tier_rate +
                   self.second_tier_limit * self.second_tier_rate +
                   (taxable_amount - self.second_tier_limit) * self.third_tier_rate)
        return tax

transactions = [100000, 200000, 150000, 50000]
calculator = ITCalculator(transactions)
tax = calculator.calculate_tax()
print(f"Tax: {tax}")