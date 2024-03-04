import threading
import random
import time

N = 5  # number of philosophers
MAX_MEALS = 100  # number of meals each philosopher should eat
forks = [threading.Lock() for i in range(N)]  # one fork per philosopher


def philosopher(i):
    meals = 0
    while meals < MAX_MEALS:
        # think for a while
        print(f"Philosopher {i} is meditating.")
        time.sleep(random.uniform(0, 1))

        # pick up forks
        fork1 = forks[i]
        fork2 = forks[(i + 1) % N]
        while True:
            if fork1.acquire(blocking=False):
                if fork2.acquire(blocking=False):
                    break
                else:
                    fork1.release()
            time.sleep(random.uniform(0, 1))

        # eat for a while
        print(f"Philosopher {i} is eating.")
        time.sleep(random.uniform(0, 1))

        # put down forks
        fork1.release()
        fork2.release()

        meals += 1


# create and start philosopher threads
threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    t.start()
    threads.append(t)

# wait for all threads to finish
for t in threads:
    t.join()

print("All philosophers have finished their meals.")