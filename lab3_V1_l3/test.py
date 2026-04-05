import unittest
from lab3_V1_l3 import BinaryTree, find_successor


class TestFindSuccessor(unittest.TestCase):
    def setUp(self):
   
        self.root = BinaryTree(10)
        self.root.left = BinaryTree(5, parent=self.root)
        self.root.right = BinaryTree(15, parent=self.root)

        self.root.left.left = BinaryTree(3, parent=self.root.left)
        self.root.left.right = BinaryTree(7, parent=self.root.left)

        self.root.right.right = BinaryTree(20, parent=self.root.right)
        self.root.right.right.left = BinaryTree(12, parent=self.root.right.right)

    def test_successor_of_7(self):
        node = self.root.left.right  
        successor = find_successor(self.root, node)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 10)

    def test_successor_of_5(self):
        node = self.root.left  
        successor = find_successor(self.root, node)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 7)

    def test_successor_of_10(self):
        node = self.root  
        successor = find_successor(self.root, node)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 15)

    def test_successor_of_15(self):
        node = self.root.right  
        successor = find_successor(self.root, node)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 12)

    def test_successor_of_12(self):
        node = self.root.right.right.left  
        successor = find_successor(self.root, node)
        self.assertIsNotNone(successor)
        self.assertEqual(successor.value, 20)

    def test_successor_of_20(self):
        node = self.root.right.right  
        successor = find_successor(self.root, node)
        self.assertIsNone(successor)


if __name__ == "__main__":
    unittest.main()