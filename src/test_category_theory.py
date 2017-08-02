import unittest
from category_theory import memoize
from category_theory import factorial
from category_theory import randgen
from random import randrange

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        memoized = memoize(lambda x: x*2)
        for i in range(0, 10):
            self.assertEqual(i*2, memoized(i))
        for i in range(0, 10):
            self.assertEqual(i*2, memoized(i))

    def test_memoize_on_seeded_random_generator(self):
        mrandgen = memoize(randgen)
        for i in range(0, 100):
            for j in range(0, 5):
                self.assertEqual(mrandgen(i), randgen(i))


    def test_memoized_factorial(self):
        mfact = memoize(factorial)
        for x in range(2, 102):
            for i in range(2, 5):
                self.assertEqual(mfact(x), factorial(x))

class ExpectedFailureMemoizeCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_memoize_on_random_generator(self):
        rangen = memoize(randrange)
        val3 = randrange(1000)
        val2 = rangen(1000)
        self.assertEqual(val2, val3)
        val1 = rangen(1000)
        self.assertEqual(val1, val2)

if __name__ == "__main__":
    unittest.main()
