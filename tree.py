class Node:
    def __init__(self,val, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
def preOrder(n):
        if not n:
            return 
        
        print(n.val,end=" ")
        preOrder(n.left)
        preOrder(n.right)
        
def postOrder(n):
    if not n:
        return 
        
    postOrder(n.left)
    postOrder(n.right)
    print(n.val,end = " ")
    
def inOrder(n):
    if not n:
        return 
        
    inOrder(n.left)
    print(n.val,end = " ")
    inOrder(n.right)
    
    
def DFS(n: Node):
    stack = [n]
    
    while stack:
        a = stack.pop()
        print(a,end=" ")
        if a.right: stack.append(a.right)
        if a.left: stack.append(a.left)
        


n = Node(10)
a = Node(7)
b = Node(8)
c = Node(9)
d = Node(11)
e = Node(12)
h = Node(13)
n.right = e
n.left = b
b.left = a
b.right = c
e.left = d
e.right = h

preOrder(n)
print()
postOrder(n)
print()
inOrder(n)
print()
DFS(n)
