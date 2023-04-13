import unittest
from unittest.mock import patch
import random, threading
from farm import Farm

class TestFarm(unittest.TestCase):
    def test_init(self):
        farm = Farm(10)
        self.assertEqual(farm.INITIAL_NUMBER_FRUITS, 10)
        self.assertEqual(farm.tree_fruits, 10)
        self.assertEqual(farm.dirty_basket, 0)
        self.assertEqual(farm.virtual_dirty_basket, 0)
        self.assertEqual(farm.clean_basket, 0)
        self.assertEqual(sum(farm.farmer_fruits), 0)
        self.assertEqual(sum(farm.cleaner_fruits), 0)
        self.assertEqual(type(farm.lock_pick), type(threading.Lock()))
        self.assertEqual(type(farm.lock_clean), type(threading.Lock()))

    def test_pick_fruit(self):
        farm = Farm(2)
        thread = threading.Thread(target=farm.pick_fruit, args=(0,))

        thread.start()
        thread.join(timeout=20)
        
        self.assertEqual(farm.dirty_basket, 2)
        self.assertEqual(farm.virtual_dirty_basket, 2)
        self.assertEqual(farm.tree_fruits, 0)

    def test_clean_fruit(self):
        farm = Farm(2)
        thread = threading.Thread(target=farm.clean_fruit, args=(0,))

        farm.tree_fruits = 0
        farm.dirty_basket = 2
        farm.virtual_dirty_basket = 2

        thread.start()
        thread.join(timeout=20)
        
        self.assertEqual(farm.tree_fruits, 0)
        self.assertEqual(farm.dirty_basket, 0)
        self.assertEqual(farm.virtual_dirty_basket, 0)
        self.assertEqual(farm.clean_basket, 2)
