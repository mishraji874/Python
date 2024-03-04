numbers = [1, 2, 3]
new_numbers = [i + 1 for i in numbers]
print(new_numbers)

name = "Angela"
new_name = [i for i in name]
print(new_name)

#challenge
range_list = [i for i in range(1, 5)]
new_range = [i * 2 for i in range(1, 5)]
print(range_list)
print(new_range)

#conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddle"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

#challenge
five_names = [name.upper() for name in names if len(name) > 5]
print(five_names)