phone_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(phone_list, key=lambda x: x['make'])

print("Sorted list of dictionaries:")
print(sorted_list)