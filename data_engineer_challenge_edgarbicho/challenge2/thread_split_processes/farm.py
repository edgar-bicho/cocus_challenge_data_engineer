import threading
import time, random
from timeit import default_timer as timer

FRUITS_IN_FARM = 10

class Farm():
    def __init__(self, INITIAL_NUMBER_FRUITS) -> None:
        self.INITIAL_NUMBER_FRUITS = INITIAL_NUMBER_FRUITS
        self.tree_fruits = INITIAL_NUMBER_FRUITS
        self.dirty_basket = 0
        self.virtual_dirty_basket = 0 # acts as a semaphore: ensure resource is locked (dirty_basket) but cause no "visual" trouble while printing log status
        self.clean_basket = 0
        self.farmer_fruits =  [0] * 3
        self.cleaner_fruits =  [0] * 3
        self.lock_pick = threading.Lock()
        self.lock_clean = threading.Lock()

    def pick_fruit(self, farmer_index):
        while (1):
            with self.lock_pick:
                if (self.tree_fruits == 0):
                    break

                time_to_sleep = random.randint(3, 6)
                time.sleep(time_to_sleep-1) # picking fruit from tree
                self.tree_fruits-=1
                self.farmer_fruits[farmer_index] += 1

            time.sleep(1) # dropping fruit to dirty basket, other thread is free to pick fruit
            with self.lock_pick:
                self.dirty_basket+=1
                self.virtual_dirty_basket+=1
                self.farmer_fruits[farmer_index] -= 1

    def clean_fruit(self, cleaner_index):
        while (1):
            with self.lock_clean:
                
                clean_in_progress = False
                time_to_sleep = random.randint(2,4)

                if self.clean_basket >=  self.INITIAL_NUMBER_FRUITS:
                    break
                    
                # once dirty basket is only decreased later, its needed to do kind of "reservation" so no more than a thread picks the same fruits several times resulting in negative values
                if self.virtual_dirty_basket > 0 :
                    clean_in_progress = True
                    self.virtual_dirty_basket -= 1
        
            if clean_in_progress == True:
                time.sleep(1) # getting dirty fruit
                with self.lock_clean:
                    self.dirty_basket-=1
                    self.cleaner_fruits[cleaner_index] += 1
                time.sleep(time_to_sleep-1) # cleaning fruit
                with self.lock_clean:
                    self.clean_basket += 1
                    self.cleaner_fruits[cleaner_index] -= 1


    def log(self, ):
        start = timer()

        while (self.clean_basket<self.INITIAL_NUMBER_FRUITS):
            print(int(timer()-start), "seconds - tree:","{:02d}".format(self.tree_fruits),"- dirty_basket", "{:02d}".format(self.dirty_basket), "- clean basket ", "{:02d}".format(self.clean_basket), "- farmer1", self.farmer_fruits[0], "- farmer2", self.farmer_fruits[1], "- farmer3", self.farmer_fruits[2], "- cleaner1 ", self.cleaner_fruits[0], "- cleaner2 ", self.cleaner_fruits[1], "- cleaner3 ", self.cleaner_fruits[2])
            time.sleep(1)

            if (self.tree_fruits+self.dirty_basket+self.clean_basket+self.farmer_fruits[0]+self.farmer_fruits[1]+self.farmer_fruits[2]+self.cleaner_fruits[0]+self.cleaner_fruits[1]+self.cleaner_fruits[2] != self.INITIAL_NUMBER_FRUITS):
                print("Houston, we have a problem!")

        print(int(timer()-start), "seconds - tree:","{:02d}".format(self.tree_fruits),"- dirty_basket", "{:02d}".format(self.dirty_basket), "- clean basket ", "{:02d}".format(self.clean_basket), "- farmer1", self.farmer_fruits[0], "- farmer2", self.farmer_fruits[1], "- farmer3", self.farmer_fruits[2], "- cleaner1 ", self.cleaner_fruits[0], "- cleaner2 ", self.cleaner_fruits[1], "- cleaner3 ", self.cleaner_fruits[2])

if __name__=='__main__':
    farm = Farm(FRUITS_IN_FARM)

    threads_farmer = []
    threads_cleaner = []
    for i in range(0,3):
        threads_farmer.append(threading.Thread(target=farm.pick_fruit, args=(i,)))
        threads_cleaner.append(threading.Thread(target=farm.clean_fruit, args=(i,)))
    thread_time = threading.Thread(target=farm.log)

    thread_time.start()
    for i in range(0,3):
        threads_farmer[i].start()
        threads_cleaner[i].start()


    for i in range(0,3):
        threads_farmer[i].join()
        threads_cleaner[i].join()
    thread_time.join()
