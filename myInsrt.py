
def InsertSort(alist):
    for i  in range (1,len(alist)):#每一次 ，已经排序好的队列
        for j  in range(i,0,-1):#从前面待插入位置找
            if alist[j]<alist[j-1]: #统一向后移
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist


mylist=InsertSort([7,6,5,4,3,2,1])
print(mylist)


