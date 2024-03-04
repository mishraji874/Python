n = int(input("Enter the number: "))
is_prime = True
for i in range(2, n):
    if n % i == 0:
        print("Not leap year")
    else:
        print("Leap year")
