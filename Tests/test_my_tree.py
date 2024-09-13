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






