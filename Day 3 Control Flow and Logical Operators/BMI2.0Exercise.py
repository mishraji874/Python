#height = float(input("enter your height in m: "))
#weight = int(input("enter your weight in kg: "))
#bmi = round(weight / height ** 2)
bmi = 40
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
elif bmi > 35:
    print(f"Your bmi is {bmi}, you are clinically obese")