def dfs(root):
    if not root:
        return
    dfs(root.left)
    print(root)
    dfs(root.right)
#数组转Tree

class Node():
    def __init__(self,val,l=None,r=None):
        self.val=val
        self.left=l
        self.right=r


class Tree():
    def __init__(self,alist):
        self.alist=alist
        self.n=len(alist)
        self.root=Node(alist[0])
    def build(self,i): 
        if i==0:
            node=self.root
        else:
            node=Node(self.alist[i])
        if 2*i+2<=self.n-1:
            node.left=self.build(2*i+1)
            node.right=self.build(2*i+2)
        elif 2*i+1<=self.n-1:
            node.left=self.build(2*i+1)
            node.right=None
        else:
            node.left=None
            node.right=None
        return  node

alist=[1,2,3,4,5,6,7,8]        
b=Tree(alist)

b.build(0)
# print(b.root.val)
# print(b.root.right.val)
# print(b.root.right.right.val)
# print(b.root.left.val)
# print(b.root.right.left.val)
# print(b.root.left.left.val)


# print_bitree(b.root)

def inOrderTraverse(node):
    if node is None:
        return None
    
    print(node.val)
    inOrderTraverse(node.left)
    inOrderTraverse(node.right)

inOrderTraverse(b.root)

