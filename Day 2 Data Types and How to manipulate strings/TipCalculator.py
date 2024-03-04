print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tip_as_percent = percentage_tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

#if the bill was $150.00, split between 5 people, with 12% tip
#each person should pay (150.00 / 5) * 1.12

print(f"Each person should pay: ${final_amount}")

# we can also use {:.2f} for rounding of the digits