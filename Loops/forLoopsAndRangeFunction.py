"""
Range

for number in range(a, b)
    print(number)
"""

for number in range(1, 10): #it will print the number from 1 to 9
    print(number)

for number in range(1, 11, 3): #in this the range is from 1 to 11 and 3 is the gap between the numbers i.e. it will start from 1 and then goes to 4 and then 7 and then 10
    print(number)


#printing the sum of numbers from 1 to 100
total = 0
for number in range(1, 101):
    print(sum(number))
print(total)