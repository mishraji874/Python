def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(3, 4, 6, 2, 1, 7, 4, 3))

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)