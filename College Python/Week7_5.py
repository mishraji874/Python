import threading
import time
import random

class BarberShop:
    def __init__(self):
        self.chairs = 3 # number of waiting chairs
        self.customers = 0 # number of customers currently in the shop
        self.barber = threading.Lock() # for mutual exclusion
        self.customer = threading.Semaphore(0) # for signaling customer arrival
        self.barber_ready = threading.Semaphore(0) # for signaling barber availability
        self.barber_asleep = True # start with barber asleep

    def customer_thread(self, id):
        while True:
            self.barber.acquire() # enter barber shop
            if self.customers < self.chairs:
                self.customers += 1 # sit down in waiting chair
                print(f"Customer {id} is waiting in the barber shop with {self.customers} customers")
                self.barber.release() # release barber shop lock
                self.customer.release() # signal barber that a customer has arrived
                self.barber_ready.acquire() # wait for barber to be ready
                self.get_haircut(id) # get a haircut
            else:
                print(f"Customer {id} is leaving because the barber shop is full")
                self.barber.release() # leave barber shop
                time.sleep(random.randint(1, 3)) # go do something else for a while

    def barber_thread(self):
        while True:
            self.customer.acquire() # wait for a customer to arrive
            self.barber.acquire() # enter barber shop
            self.customers -= 1 # stand up from waiting chair
            self.barber_asleep = False # wake up barber
            print(f"Barber is cutting hair of customer {self.customers + 1}")
            time.sleep(random.randint(1, 5)) # simulate hair cutting time
            if self.customers == 0:
                self.barber_asleep = True # barber goes to sleep if no more customers
            self.barber.release() # leave barber shop
            self.barber_ready.release() # signal customer that haircut is done

    def get_haircut(self, id):
        print(f"Customer {id} is getting a haircut")
        time.sleep(random.randint(1, 5)) # simulate haircut time

if __name__ == "__main__":
    barber_shop = BarberShop()
    barber_thread = threading.Thread(target=barber_shop.barber_thread)
    barber_thread.start()
    for i in range(1, 11):
        customer_thread = threading.Thread(target=barber_shop.customer_thread, args=(i,))
        customer_thread.start()