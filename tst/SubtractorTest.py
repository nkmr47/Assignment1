import unittest
from src.Subtractor import Subtractor

class SubtractorTest(unittest.TestCase):
    def test_subtract(self):
        a = Subtractor()
        self.assertEqual(a.subtract(2, 3), -1)
        self.assertEqual(a.subtract(-1, 1), -2)
        self.assertEqual(a.subtract(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
