import unittest
from mytree import MyTree

class TestMyTree(unittest.TestCase):

    def test_create_empty_tree(self):
        tree = MyTree()
        self.assertIsNone(tree.root)

    def test_create_empty_tree(self):
        tree = MyTree()
        self.assertIsNone(tree.root)

    def test_add_value_to_tree(self):
        tree = MyTree()
        tree.add(5)
        self.assertFalse(tree.is_empty())


    def test_tree_contains_value(self):
         tree = MyTree()
         tree.add(5)
         self.assertTrue(tree.contains(5))
         self.assertFalse(tree.contains(10))






