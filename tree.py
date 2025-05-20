from collections import deque


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
        

def BFS(n):
    b = deque()
    b.append(n)
    while b:
        a = b.popleft()
        print(a,end = " ")
        if a.left: b.append(a.left)
        if a.right: b.append(a.right)
    

def checkBST(n: Node, v):
    if not n:
        return False
    
    if n.val == v:
        return True
    
    if n.val < v:
        return checkBST(n.right,v)
    return checkBST(n.left,v)
    

def hasPathSum(root: Node, v: int):
    def pathSum(root: Node, cs):
        if not root:
            return False
    
        cs += root.val
    
        if not root.left and not root.right :
            return cs == v
    
        return pathSum(root.left,cs) or pathSum(root.right,cs)
    
    return pathSum(root,0)
        

def isBalanced(n: Node):
    balanced = [True]
    def path(n: Node):
        if not n:
            return 0
        
        left = path(n.left)
        right = path(n.right)
        
        if abs(left - right) > 1:
            balanced[0] = False
            return 0
        
        return 1+max(left, right)
    
    path(n)
    return balanced[0]

        
    
n = Node(10)
a = Node(7)
b = Node(8)
c = Node(9)
d = Node(11)
e = Node(12)
h = Node(13)
i = Node(14)
j = Node(15)
n.right = e
n.left = b
b.left = a
b.right = c
e.left = d
e.right = h
h.right = i
# i.right = j

print(hasPathSum(n,27))
print(isBalanced(n))