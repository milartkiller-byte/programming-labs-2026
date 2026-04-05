import unittest
from lab2_1_2 import max_hamsters


class TestMaxHamsters(unittest.TestCase):
    def test_example_1(self):
        S = 7
        hamsters = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamsters(S, hamsters), 2)

    def test_example_2(self):
        S = 19
        hamsters = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamsters(S, hamsters), 3)

    def test_example_3(self):
        S = 2
        hamsters = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamsters(S, hamsters), 1)

    def test_zero_possible(self):
        S = 0
        hamsters = [[1, 1], [2, 2]]
        self.assertEqual(max_hamsters(S, hamsters), 0)

    def test_all_possible(self):
        S = 100
        hamsters = [[1, 0], [2, 0], [3, 0]]
        self.assertEqual(max_hamsters(S, hamsters), 3)

    def test_one_hamster(self):
        S = 5
        hamsters = [[5, 100]]
        self.assertEqual(max_hamsters(S, hamsters), 1)


if __name__ == "__main__":
    unittest.main()