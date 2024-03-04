class Bank:
    def __init__(self):
        self.customers = []
        self.services = {"service1": [], "service2": [], "service3": []}

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_rating(self, customer, service, rating, date):
        self.services[service].append((customer, rating, date))

    def display_total_score(self, service):
        total_score = 0
        for customer, rating, date in self.services[service]:
            total_score += rating
        print("Total score for " + service + ": " + str(total_score))

    def display_customer_score(self, customer, service):
        customer_score = 0
        for c, rating, date in self.services[service]:
            if c == customer:
                customer_score += rating
        print("Score for " + customer + " for " + service + ": " + str(customer_score))

class Customer:
    def __init__(self, name):
        self.name = name

    def rate_service(self, bank, service, rating, date):
        bank.add_rating(self, service, rating, date)

bank = Bank()

customer1 = Customer("customer1")
customer2 = Customer("customer2")

bank.add_customer(customer1)
bank.add_customer(customer2)

while True:
    print("\nSelect the service you want to rate:")
    print("1. service1")
    print("2. service2")
    print("3. service3")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        service = "service1"
    elif choice == 2:
        service = "service2"
    elif choice == 3:
        service = "service3"
    elif choice == 4:
        break
    else:
        continue

    rating = int(input("Enter your rating for " + service + " (1-5): "))
    date = input("Enter the date: ")
    customer1.rate_service(bank, service, rating, date)
    bank.display_total_score(service)
    bank.display_customer_score(customer1.name, service)