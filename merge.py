def merge(leftP,rightP):
    i,j=0,0
    blist=[]
    while i < len(leftP) and j <len(rightP):
        if leftP[i] <= rightP[j]:
            blist.append(leftP[i])
            i += 1
        else:
            blist.append(rightP[j])
            j += 1
    blist += rightP[j:] if i == len(leftP) else leftP[i:]

    return blist


def MergeSort(alist):

    n = len(alist)
    if n <=1 :
        return alist
    else :
        mid = n // 2
        left = MergeSort(alist[:mid])
        right = MergeSort(alist[mid:])
        return merge(left,right) 


print(MergeSort([34,678,89,23,4455]))