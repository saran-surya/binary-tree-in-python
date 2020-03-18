class node:
    def __init__(self, data):
        self.data = data                            #initial node constuctor of nodes in bst
        self.left = self.right = None

class bst(node):
    def __init__(self):
        self.root = None
    
    def append(self,data):
        if not self.root:                       # passing the values to helper function
            self.root = node(data)
        else:
            self._add(self.root, data)

    def _add(self, start, data):                #adding nodes to the binary tree
        if data < start.data:
            if not start.left:
                start.left = node(data)
            else:
                self._add(start.left, data)
        else:
            if not start.right:
                start.right = node(data)
            else:
                self._add(start.right, data)
        
    def lca(self, root, node1, node2):          #function to find Least common ancestor
        if not root:
            return None
        if root.data == node1 or root.data == node2:
            return root.data
        left_lca = self.lca(root.left, node1, node2)
        right_lca = self.lca(root.right, node1, node2)
        if left_lca and right_lca:
            return root.data
        return left_lca if left_lca is not None else right_lca

a = bst()
b = list(map(int,input().split()))    
for i in b:
    a.append(i)
x, y = map(int,input().split())
ans = a.lca(a.root, x, y)                 #passing the nodes to calculate Least Common Ancestor
print(ans)
