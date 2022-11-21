from unicodedata import name


class Node():
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.rchild = None
        self.lchild = None


class HuffmanTree():
    def __init__(self, Name_Value):
        self.InitNode = [Node(NV[0], NV[1]) for NV in Name_Value]
        while len(self.InitNode) != 1:
            self.InitNode.sort(key=lambda NV: NV.value, reverse=True)
            SumNode = Node(
                value=(self.InitNode[-1].value+self.InitNode[-2].value))
            SumNode.lchild = self.InitNode.pop(-1)
            SumNode.rchild = self.InitNode.pop(-1)
            self.InitNode.append(SumNode)
        self.root = self.InitNode[0]
        # print(self.InitNode)
        self.Buffer = list(range(10))

    def RecursiveTrace01(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:#碰到叶节点 才会
            print(node.name + "编码为", end=""),
            # print(length)
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.RecursiveTrace01(node.lchild, length+1)
        self.Buffer[length] = 1
        self.RecursiveTrace01(node.rchild, length+1)

    def getHuffCode(self):
        self.RecursiveTrace01(self.root, 0)
    


NVTest = [('a', 6), ('b', 4), ('c', 10), ('d', 8), ('f', 12), ('g', 2)]
MyTree = HuffmanTree(NVTest)
MyTree.getHuffCode()
