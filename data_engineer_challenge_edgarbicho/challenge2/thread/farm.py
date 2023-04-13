import threading
import time, random
from timeit import default_timer as timer

INITIAL_NUMBER_FRUITS = 50
tree_fruits = INITIAL_NUMBER_FRUITS
dirty_basket = 0
clean_basket = 0
farmer_fruits = [0 , 0, 0]
cleaner_fruits = [0 , 0 ,0]
lock_pick = threading.Lock()
lock_clean = threading.Lock()

def pick_fruit(farmer_index):
    global tree_fruits, dirty_basket, farmer_fruits, lock_pick

    while (1):
        with lock_pick:
            if (tree_fruits == 0):
                break

            tree_fruits-=1
            farmer_fruits[farmer_index] += 1

            time_to_sleep = random.randint(3, 6)
            print("farmer", farmer_index+1 , "picking for", time_to_sleep , "seconds.")

            time.sleep(time_to_sleep)

            print("farmer", farmer_index+1, "dropped to dirty basket.")
            dirty_basket+=1
            farmer_fruits[farmer_index] -= 1

        time.sleep(0.1) # trick which helps thread rotation and not keeping same farmer


def clean_fruit(cleaner_index):
    global dirty_basket, clean_basket, cleaner_fruits, lock_clean, INITIAL_NUMBER_FRUITS

    while (1):
        with lock_clean:

            clean_in_progress = False
            time_to_sleep = random.randint(2,4)

            if clean_basket >=  INITIAL_NUMBER_FRUITS:
                break

            if dirty_basket > 0 :
                clean_in_progress = True
                dirty_basket -= 1
                cleaner_fruits[cleaner_index] += 1
                
                print("cleaner", cleaner_index+1 , "cleaning for", time_to_sleep, "seconds.")
        
        time.sleep(time_to_sleep) # like this sleeps wether work is done or not
        if clean_in_progress == True:
            #time.sleep(time_to_sleep) # case only sleeps if work is done
            with lock_clean:
                print("cleaner", cleaner_index+1 , "dropped to clean basket.")
                clean_basket += 1
                cleaner_fruits[cleaner_index] -= 1


def log():
    global tree_fruits, dirty_basket, clean_basket, farmer_fruits, cleaner_fruits, INITIAL_NUMBER_FRUITS
    start = timer()
    while (clean_basket<INITIAL_NUMBER_FRUITS):
        print(int(timer()-start), "seconds - tree:","{:02d}".format(tree_fruits),"- dirty_basket", "{:02d}".format(dirty_basket), "- clean basket ", "{:02d}".format(clean_basket), "- farmer1", farmer_fruits[0], "- farmer2", farmer_fruits[1], "- farmer3", farmer_fruits[2], "- cleaner1 ", cleaner_fruits[0], "- cleaner2 ", cleaner_fruits[1], "- cleaner3 ", cleaner_fruits[2])
        time.sleep(1)
    print(int(timer()-start), "seconds - tree:","{:02d}".format(tree_fruits),"- dirty_basket", "{:02d}".format(dirty_basket), "- clean basket ", "{:02d}".format(clean_basket), "- farmer1", farmer_fruits[0], "- farmer2", farmer_fruits[1], "- farmer3", farmer_fruits[2], "- cleaner1 ", cleaner_fruits[0], "- cleaner2 ", cleaner_fruits[1], "- cleaner3 ", cleaner_fruits[2])  

if __name__=='__main__':
    threads_farmer = []
    threads_cleaner = []
    for i in range(0,3):
        threads_farmer.append(threading.Thread(target=pick_fruit, args=(i,)))
        threads_cleaner.append(threading.Thread(target=clean_fruit, args=(i,)))
    thread_time = threading.Thread(target=log)

    thread_time.start()
    for i in range(0,3):
        threads_farmer[i].start()
        threads_cleaner[i].start()

