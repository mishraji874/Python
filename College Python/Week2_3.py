def move_zeros_to_end(numbers):
    zero_count = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            zero_count += 1
        else:
            numbers[i - zero_count], numbers[i] = numbers[i], numbers[i - zero_count]
    return numbers

numbers = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print("Original list:", numbers)
print("List after moving zeros to end:", move_zeros_to_end(numbers))