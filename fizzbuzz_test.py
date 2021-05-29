import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(fizzbuzz.fb(3), "Fizz")

    def test0(self):
        self.assertEqual(fizzbuzz.fb(5), "Buzz")

    def test1(self):
        self.assertEqual(fizzbuzz.fb(15), "FizzBuzz")
    
    def test2(self):
        self.assertEqual(fizzbuzz.fb(4), 4)

if __name__ == '__main__':
    unittest.main()