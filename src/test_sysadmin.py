import unittest
from sysadmin import list_all_files
from sysadmin import get_page
from sysadmin import memoize
from sysadmin import factorial
from random import randrange

class TestListAllFiles(unittest.TestCase):
    def test_does_not_crash_on_empty_path(self):
        actual = [x for x in list_all_files(None)]
        self.assertEqual([], actual)

    def test_inspect_directory_above(self):
        actual = [x for x in list_all_files('../')]
        self.assertGreater(len(actual), 0)

    def test_get_page(self):
        self.assertEqual(True, get_page('https://google.com'))


    def test_memoize(self):
        memoized = memoize(lambda x: x*2)
        for i in range(0, 10):
            self.assertEqual(i*2, memoized(i))
        for i in range(0, 10):
            self.assertEqual(i*2, memoized(i))

class TestMemoize(unittest.TestCase):
    def test_memoize_on_random_generator(self):
        rangen = memoize(randrange)
        val3 = randrange(1000)
        val2 = rangen(1000)
        self.assertEqual(val2, val3)
        val1 = rangen(1000)
        self.assertEqual(val1, val2)


    def test_memoized_factorial(self):
        mfact = memoize(factorial)
        for x in range(2, 102):
            for i in range(2, 5):
                self.assertEqual(mfact(x), factorial(x))

if __name__ == '__main__':
    unittest.main()
