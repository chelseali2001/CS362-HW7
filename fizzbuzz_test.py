import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(fizzbuzz.fb(3), "Fizz")

if __name__ == '__main__':
    unittest.main()