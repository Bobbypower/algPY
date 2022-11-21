# class CPath():
#     def __init__(self):
#         print("init")
inf=float("inf")
G=[
    [0,3,2,inf,inf,inf],
    [inf,0,inf,2,3,0],
    [inf,inf,0,4,inf,3],
    [inf,inf,inf,0,inf,2],
    [inf,inf,inf,inf,0,1],
    [inf,inf,inf,inf,inf,0]

]
tq=[0,2,1,4,3,5]
Ve=[0]*len(G)
def early(tq1,G1,node):
    for i   in  range(len(G)):
        if G[i][node] != 0 and G[i][node] != inf :
            TempVe=Ve[i]+G[i][node]
            if TempVe > Ve[node]:
                Ve[node]=TempVe
    # print(Ve)
def late(tq1,G1,node):
    for i   in  range(len(G)):
        # print
        if G[i][node] != 0 and G[i][node] != inf :
            TempVl=Vl[node]-G[i][node]
            print(TempVl)
            if TempVl < Vl[i]:
                Vl[i]=TempVl
    print(Vl)

early(tq,G,2)
early(tq,G,1)
early(tq,G,4)
early(tq,G,3)
early(tq,G,5)
Vl=[Ve[-1]]*len(G)
print(Vl)

late(tq,G,5)
late(tq,G,3)
late(tq,G,4)
late(tq,G,1)
late(tq,G,2)
late(tq,G,0)

for i in range(len(G)):
    if Vl[i]-Ve[i]==0:
        print(i)
    
    