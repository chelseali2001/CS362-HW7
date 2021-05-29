import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(fizzbuzz.fb(3), "Fizz")

    def test0(self):
        self.assertEqual(fizzbuzz.fb(5), "Buzz")

if __name__ == '__main__':
    unittest.main()