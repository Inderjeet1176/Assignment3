class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MyTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._remove(node.right, temp.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(node.left, value)
        else:
            return self._contains(node.right, value)

    def is_sorted(self):
        return self._is_sorted(self.root, float('-inf'), float('inf'))

    def _is_sorted(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value <= max_value):
            return False
        return self._is_sorted(node.left, min_value, node.value) and self._is_sorted(node.right, node.value, max_value)
