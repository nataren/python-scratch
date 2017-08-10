import unittest
import solutions

class TestSolutions(unittest.TestCase):
    def test_indices_that_add_to_target(self):
        indices = solutions.indices_that_add_to_target([1,3,5,7], 12)
        self.assertEqual(2, indices[0])
        self.assertEqual(3, indices[1])

if __name__ == '__main__':
    unittest.main()
