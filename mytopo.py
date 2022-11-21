
inf=float("inf")
def TopologicalSort(G):
    # print(G[3])
    indegreeG=[0]*len(G)
    for i  in  range(len(G)):
        for j  in  range(len(G)):
            if G[j][i] == 0 or  G[j][i] == inf:
                continue
            else:
                # print(G[j][i])
                indegreeG[i]+=1
    print(indegreeG)
    Q=[v  for  v  in  range(len(indegreeG)) if indegreeG[v]==0]
    # print(Q)
    S=[]  #记录已经访问过的节点 万一有环路呢
    while Q:
        vnow=Q.pop()
        print(vnow)
        S.append(vnow)
        for  i  in  range(len(G[vnow])):
            if G[vnow][i] == 0 or  G[vnow][i] == inf:
                print(G[i][vnow])
                continue
            else:
                indegreeG[i]-=1
            if indegreeG[i]==0:
                Q.append(i)
    if len(G) == len(S):
        return  S
    else:
        return None
G=[
    [0,3,2,inf,inf,inf],
    [inf,0,inf,2,3,0],
    [inf,inf,0,4,inf,3],
    [inf,inf,inf,0,inf,2],
    [inf,inf,inf,inf,0,inf],
    [inf,inf,inf,inf,inf,0]

]

print(TopologicalSort(G))
