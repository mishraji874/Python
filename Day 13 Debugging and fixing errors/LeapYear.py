n = int(input("Enter year: "))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")