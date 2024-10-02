class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Lowest_Common_Ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    
    left = Lowest_Common_Ancestor(root.left, p, q)
    right = Lowest_Common_Ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

# Test Case 1
root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = find_node(root, 5)
q = find_node(root, 4)
lca = Lowest_Common_Ancestor(root, p, q)
print(lca.val)

# Test Case 2
p = find_node(root, 5)
q = find_node(root, 1)
lca = Lowest_Common_Ancestor(root, p, q)
print(lca.val)

#Test case 3
root = build_tree([1, 2])
p = find_node(root, 1)
q = find_node(root, 2)
lca = Lowest_Common_Ancestor(root, p, q)
print(lca.val)  # Expected output: 1
