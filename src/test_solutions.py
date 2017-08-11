import unittest
import solutions

class TestSolutions(unittest.TestCase):
    def test_indices_that_add_to_target_1(self):
        indices = solutions.indices_that_add_to_target_cuadratic([1,3,5,7], 12)
        self.assertEqual(2, indices[0])
        self.assertEqual(3, indices[1])

    def test_indices_that_add_to_target_2(self):
        indices = solutions.indices_that_add_to_target_cuadratic([1,3,5,7], 8)
        self.assertEqual(0, indices[0])
        self.assertEqual(3, indices[1])

    def test_indices_that_add_to_target_linear(self):
        indices = solutions.indices_that_add_to_target_linear([3,2,4], 6)
        self.assertEqual([1,2], indices)

if __name__ == '__main__':
    unittest.main()
