def Merge(LPart,RPart):
    i,j=0,0
    blist=[]
    while i < len(LPart) and j < len(RPart):    
        if LPart[i] <= RPart[j]:
            blist.append(LPart[i])
            i=i+1
        else:
            blist.append(RPart[j])
            j=j+1

    blist+=RPart[j:] if i==len(LPart)  else  LPart[i:]

    return blist
def MergeSort(mylist):
    n=len(mylist)
    if n <=1:
        return mylist
    else:
        mid=n//2
        left=MergeSort(mylist[:mid])
        right=MergeSort(mylist[mid:])
        return Merge(left,right)
    
myList=[5,4,3,2,1,-1]
print(MergeSort(myList))


