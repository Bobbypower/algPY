NVTest=[("A",2),("B",3),("C",1),("D",7),("E",4),("F",2),("G",9),("H",1)]
class Node():
    def __init__(self,name=None,value=None,):
        self.name=name
        self.value=value
        self.lchile=None
        self.rchild=None
        # self.buffer=list(len(NVTest))

class HuffmanTree():
    def __init__(self,N_V):
        self.InitNode=[Node(NV[0],NV[1]) for NV in  N_V]
        while len(self.InitNode) <= 1:
            self.InitNode.sort(key=lambda NV:NV.value,reverse=True)
            SumNode=Node(self.InitNode[-1].value+self.InitNode[-2].value)
            SumNode.lchild=self.InitNode.pop(-1)
            SumNode.rchild=self.InitNode.pop(-1)
            self.InitNode.append(SumNode)
        self.root=self.InitNode[0]
        self.buffer = list(range(10))
    def Recursive01(self,tree,h):
        node=tree 
        if not node:
            return 
        elif node.name:
            print(node.name+"编码为:",end="")
            print("\n")
            return 
        self.buffer[h]=0
        self.Recursive01(node.left,h+1)
        self.buffer[h]=1
        self.Recursive01(node.right,h+1)        
    def getCode(self):
        self.Recursive01(self.root,0)        

MyTree = HuffmanTree(NVTest)
MyTree.getCode()
