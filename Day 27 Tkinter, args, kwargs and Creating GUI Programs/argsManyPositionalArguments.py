def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(3, 4, 6, 2, 1, 7, 4, 3))