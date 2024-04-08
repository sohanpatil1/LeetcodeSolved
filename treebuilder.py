# treebuilder.py
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class TreeBuilder:
    """
    tree = TreeBuilder([1, 2, 3, 4, 5, 6])
    """
    def __init__(self, values):
        self.index = 0
        self.root = self.build_tree(values)

    def build_tree(self, values):
        if not values:
            return None
        root = self.construct_node(values)
        self.construct_children(root, values)
        return root

    def construct_node(self, values):
        if self.index < len(values) and values[self.index] is not None:
            node = TreeNode(values[self.index])
            self.index += 1
            return node
        self.index += 1
        return None

    def construct_children(self, parent, values):
        if parent:
            parent.left = self.construct_node(values)
            parent.right = self.construct_node(values)
            self.construct_children(parent.left, values)
            self.construct_children(parent.right, values)

    # Directly return the root node
    def __getattr__(self, attr):
        return getattr(self.root, attr)

# Example usage:
if __name__ == "__main__":
    tree = TreeBuilder([1, 2, 3, 4, 5, 6])
    print(tree.val)  # Access the root node's value directly
