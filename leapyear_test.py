import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(leapyear.lp(2001), "is not a leap year")

if __name__ == '__main__':
    unittest.main()