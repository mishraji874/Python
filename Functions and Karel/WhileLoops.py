"""
FOR LOOP

for item in list_of_items:
    #do something to each item

for number in range(a, b):
    print(number)


WHILE LOOP

while something_is_true:
    #do something repeatedly
"""

i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")