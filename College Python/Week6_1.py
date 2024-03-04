import time
import math
import threading
from queue import Queue
def get_divisor_count(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def find_max_divisors(start, end, result_queue):
    max_divisors = 0
    max_num = 0
    for i in range(start, end+1):
        divisors = get_divisor_count(i)
        if divisors > max_divisors:
            max_divisors = divisors
            max_num = i
    result_queue.put((max_num, max_divisors))

if __name__ == '__main__':
    start_time = time.time()
    num_threads = 4
    range_size = 100000
    step = range_size // num_threads
    result_queue = Queue()
    threads = []
    for i in range(num_threads):
        start = i*step + 1
        end = (i+1)*step if i < num_threads-1 else range_size
        t = threading.Thread(target=find_max_divisors, args=(start, end, result_queue))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    max_num = 0
    max_divisors = 0
    while not result_queue.empty():
        num, divisors = result_queue.get()
        if divisors > max_divisors:
            max_num = num
            max_divisors = divisors
    print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
    print(f"Number with most divisors: {max_num}")
    print(f"Number of divisors: {max_divisors}")