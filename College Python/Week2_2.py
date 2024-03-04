def count_case(input_string):
    upper_count = 0
    lower_count = 0
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return (upper_count, lower_count)

input_string = "The quick Brow Fox"
upper_count, lower_count = count_case(input_string)
print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)