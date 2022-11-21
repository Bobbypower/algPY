grap = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
#存图
 
# def BFS(grap,star):                #BFS算法
#     queue = []                     #定义一个队列
#     seen = set()                   #建立一个集合，集合就是用来判断该元素是不是已经出现过
#     queue.append(star)             #将任一个节点放入
#     seen.add(star)                 #同上
#     while (len(queue)>0) :         #当队列里还有东西时
#         ver =  queue.pop(0)        #取出队头元素
#         notes = grap[ver]          #查看grep里面的key,对应的邻接点
#         for i in notes:            #遍历邻接点
#             if i not in seen:      #如果该邻接点还没出现过
#                 queue.append(i)    #存入queue
#                 seen.add(i)        #存入集合
#         print(ver)                 #打印队头元素
 
 
global inf=float("inf") 

def myBFS(G,v):
    # global inf
    aQueue=[]
    visited=[False for i in range(len(G))]
    aQueue.append(v)
    visited[v]=True
    while(len(aQueue)>0):
        _v=aQueue.pop(0)
        for i  in  range(len(G)):
            if G[_v][i] != inf and visited[i]==False:
                aQueue.append(i) 
                visited[i]=True
        print(_v)


print(myBFS([[1,1,1,0],[1,0,1,1],[1,1,0,1],[1,1,1,0]],0))