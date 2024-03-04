class Customer:
    def __init__(self, name, address, pincode):
        self.name = name
        self.address = address
        self.pincode = pincode

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}, Pincode: {self.pincode}"

customers = [
    Customer("John Doe", "123 Main St", 123456),
    Customer("Jane Doe", "456 Elm St", 654321),
    Customer("Bob Smith", "789 Oak St", 111111),
    Customer("Alice Johnson", "246 Maple Ave", 222222),
]

def find_nearby_customers(customers, name=None, pincode=None):
    nearby_customers = []
    for customer in customers:
        if name is not None and customer.name != name:
            continue
        if pincode is not None and abs(customer.pincode - pincode) > 1000:
            continue
        nearby_customers.append(customer)
    return nearby_customers

nearby_customers = find_nearby_customers(customers, pincode=123456)
for customer in nearby_customers:
    print(customer)