def find_numbers(string):
    numbers = [int(num) for num in string.split() if num.isdigit()]
    numbers = list(filter(lambda x: x > len(numbers), numbers))
    return sorted(numbers)

string = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
print("Numbers in sorted form:", find_numbers(string))