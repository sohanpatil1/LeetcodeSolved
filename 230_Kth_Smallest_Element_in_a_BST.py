from treebuilder import TreeBuilder

def kthSmallest(root, k) -> int:
    result = []
    def recur(root):
        if not root:
            return
        recur(root.left)
        result.append(root.val)
        recur(root.right)
    
    recur(root)
    return(result[k-1])

root = TreeBuilder([3,1,4,None,2])
result = kthSmallest(root=root, k=1)
print(result)