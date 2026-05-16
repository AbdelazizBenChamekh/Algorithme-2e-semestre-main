import unittest
from lab2.lab_16.src.task16 import KthMax

class TestKthMax(unittest.TestCase):
    def setUp(self):
        self.kth_max_ds = KthMax()

    def test_add_elements(self):
        self.kth_max_ds.add(5)
        self.kth_max_ds.add(3)
        self.kth_max_ds.add(7)
        self.assertEqual(self.kth_max_ds.kth_max(1), 7)
        self.assertEqual(self.kth_max_ds.kth_max(2), 5)
        self.assertEqual(self.kth_max_ds.kth_max(3), 3)

    def test_remove_element(self):
        self.kth_max_ds.add(10)
        self.kth_max_ds.add(20)
        self.kth_max_ds.remove(10)
        self.assertEqual(self.kth_max_ds.kth_max(1), 20)

    def test_kth_maximum(self):
        self.kth_max_ds.add(15)
        self.kth_max_ds.add(25)
        self.kth_max_ds.add(35)
        self.kth_max_ds.add(45)
        self.assertEqual(self.kth_max_ds.kth_max(2), 35)
        self.assertEqual(self.kth_max_ds.kth_max(4), 15)

    def test_kth_max_with_deletion(self):
        self.kth_max_ds.add(8)
        self.kth_max_ds.add(6)
        self.kth_max_ds.add(10)
        self.kth_max_ds.remove(10)
        self.assertEqual(self.kth_max_ds.kth_max(1), 8)

if __name__ == "__main__":
    unittest.main()
