import unittest
from mytree import MyTree

class TestMyTree(unittest.TestCase):

    def test_create_empty_tree(self):
        tree = MyTree()
        self.assertIsNone(tree.root)


