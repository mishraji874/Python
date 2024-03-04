import multiprocessing

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    digits = [int(x) for x in str(n)]
    num_digits = len(digits)
    sum_of_powers = sum([x ** num_digits for x in digits])
    return sum_of_powers == n

def print_odd_numbers():
    for i in range(101, 200, 2):
        print(i)

def print_prime_numbers():
    for i in range(200, 300):
        if is_prime(i):
            print(i)

def print_armstrong_numbers():
    for i in range(100, 300):
        if is_armstrong(i):
            print(i)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_odd_numbers)
    p2 = multiprocessing.Process(target=print_prime_numbers)
    p3 = multiprocessing.Process(target=print_armstrong_numbers)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()