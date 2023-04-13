import unittest
import threading
from farm import Farm

class TestFarm(unittest.TestCase):
    
    def test_farm(self):
        fruits_in_farm = 4
        farm = Farm(fruits_in_farm)
        
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
        
        self.assertEqual(farm.tree_fruits, 0)
        self.assertEqual(farm.dirty_basket, 0)
        self.assertEqual(farm.clean_basket, fruits_in_farm)
        self.assertEqual(sum(farm.farmer_fruits), 0)
        self.assertEqual(sum(farm.cleaner_fruits), 0)
