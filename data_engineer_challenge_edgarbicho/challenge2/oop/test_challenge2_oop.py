import unittest
from unittest.mock import patch
import random
from challenge2_oop_classes import Tree, Basket, Farmer, Collector, Cleaner

class TestTree(unittest.TestCase):
    def test_init(self):
        tree = Tree(10)
        self.assertEqual(tree.fruits, 10)
        self.assertFalse(tree.hasWorker)

    def test_start_collect_no_fruits(self):
        tree = Tree(0)
        tree.start_collect()
        self.assertFalse(tree.hasWorker)

    def test_start_collect_with_fruits(self):
        tree = Tree(5)
        tree.start_collect()
        self.assertTrue(tree.hasWorker)

    def test_end_collect_no_fruits(self):
        tree = Tree(0)
        tree.end_collect()
        self.assertFalse(tree.hasWorker)

    def test_end_collect_with_fruits_no_worker(self):
        tree = Tree(5)
        tree.end_collect()
        self.assertFalse(tree.hasWorker)
        self.assertEqual(tree.fruits, 5)

    def test_end_collect_with_fruits_with_worker(self):
        tree = Tree(5)
        tree.hasWorker = True
        tree.end_collect()
        self.assertFalse(tree.hasWorker)
        self.assertEqual(tree.fruits, 4)

    def test_hasFruits_true(self):
        tree = Tree(1)
        self.assertTrue(tree.hasFruits())

    def test_hasFruits_false(self):
        tree = Tree(0)
        self.assertFalse(tree.hasFruits())

class TestBasket(unittest.TestCase):
    def test_has_fruits(self):
        basket = Basket()
        self.assertFalse(basket.hasFruits())

        basket.add()
        self.assertTrue(basket.hasFruits())

        basket.remove()
        self.assertFalse(basket.hasFruits())

class TestFarmer(unittest.TestCase):
    def test_fruits_on_hand(self):
        farmer = Farmer()
        self.assertFalse(farmer.fruitsOnHand())

        farmer.hasFruitOnHand = True
        self.assertTrue(farmer.fruitsOnHand())

class TestCollector(unittest.TestCase):
    def test_is_busy(self):
        collector = Collector()
        self.assertFalse(collector.isBusy())

        collector.isPicking = True
        self.assertTrue(collector.isBusy())

        collector.isPicking = False
        collector.isDropping = True
        self.assertTrue(collector.isBusy())

    def test_work(self):
        collector = Collector()
        collector.isPicking = True
        collector.timeToFinish = 1
        collector.work()
        self.assertEqual(collector.timeToFinish, 0)
        self.assertTrue(collector.isWorkFinished())

    @patch.object(random, 'randint', return_value=2)
    def test_pick(self, randint_mock):
        collector = Collector()
        collector.pick()
        self.assertTrue(collector.isPicking)
        self.assertEqual(collector.timeToFinish, 2)

    def test_complete_work(self):
        collector = Collector()
        collector.isPicking = True
        collector.completeWork()
        self.assertTrue(collector.hasFruitOnHand)
        self.assertFalse(collector.isPicking)

class TestCleaner(unittest.TestCase):
    def test_is_busy(self):
        cleaner = Cleaner()
        self.assertFalse(cleaner.isBusy())

        cleaner.isPulling = True
        self.assertTrue(cleaner.isBusy())

        cleaner.isPulling = False
        cleaner.isCleaning = True
        self.assertTrue(cleaner.isBusy())

    def test_work(self):
        cleaner = Cleaner()
        cleaner.isCleaning = True
        cleaner.timeToFinish = 1
        cleaner.work()
        self.assertEqual(cleaner.timeToFinish, 0)
        self.assertTrue(cleaner.isWorkFinished())

    @patch.object(random, 'randint', return_value=2)
    def test_clean(self, randint_mock):
        cleaner = Cleaner()
        cleaner.clean()
        self.assertTrue(cleaner.isCleaning)
        self.assertEqual(cleaner.timeToFinish, 2)

    def test_complete_work(self):
        cleaner = Cleaner()
        cleaner.isCleaning = True
        cleaner.completeWork()
        self.assertFalse(cleaner.hasFruitOnHand)
        self.assertFalse(cleaner.isCleaning)
