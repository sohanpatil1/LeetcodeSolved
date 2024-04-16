from treebuilder import TreeBuilder, TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def addOneRow(root, val: int, depth: int):
    if not root or depth == 1:
        node = TreeNode(val=val, left=root, right=None)
        return node

    q = deque([root])
    nodesindepth = []
    curdepth = 1
    while q:    # Will always have nodes at depth. 
        node = q.popleft()
        if curdepth < depth-1:
            if node.left:
                nodesindepth.append(node.left)  # Nodes in depth will have nodes 1 below depth
            if node.right:
                nodesindepth.append(node.right)
        elif curdepth == depth - 1:
            if node.left:
                node.left = TreeNode(val=val, left=node.left, right=None)
            if node.right:
                node.right = TreeNode(val=val, left=None, right=node.right)
        else:
            return root
        if not q:
            depth += 1
            q = deque(nodesindepth)
            nodesindepth = []
    return root

root = TreeBuilder([4,2,None,3,1])
result = addOneRow(root=root, val=1, depth=2)
print(result)