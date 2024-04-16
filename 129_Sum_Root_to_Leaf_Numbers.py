from treebuilder import TreeBuilder
def sumNumbers(node) -> int:
    cumsum = 0
    def recur(node, num):
        nonlocal cumsum
        if not node.left and not node.right: # Leaf node
            print(num)
            cumsum += num
        if node.left:
            recur(node.left, (num*10)+node.left.val)
        if node.right:
            recur(node.right, (num*10)+node.right.val)
    recur(node, node.val)
    return 1

root = TreeBuilder([1,2,3])
result = sumNumbers(root)
print(result)