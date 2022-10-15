class Node():
    def __init__(self,name=None,value=None) -> None:
        self.name=name
        self.value=value
        self.rchild=None
        self.lchild=None

# class DFS():
#     def init(self):
#         self.root=None
#     def buildTree(self,treedata):
#         if not self.root:
#             self.root=Node(name=0,value=treedata[0])
#         self.rchild=Node()

inf = float("inf")
visited=[]
def DFSTravres(G):
    # print(G)
    global visited
    visited=[False]*len(G)
    # print(visited)
    for i in range(len(G)):
        if not visited[i]:
            print("这是开始遍历",i)
            DFS(G,i)
    return None

def DFS(G,v):
    print("这是调用DFS",v)
    global visited
    # print(visited)
    visited[v]=True
    for  i  in  range(len(G)):
        if G[v][i] != inf and visited[i]==False:
            DFS(G,i)
    return None


b=DFSTravres([[0,1,1],[1,0,1],[1,1,0]])
  
    