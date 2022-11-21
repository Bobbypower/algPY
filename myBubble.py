
def Bubble(alist):
    for i in range(1,len(alist)):#待排序元素个数，每次确定一个，最后一个不用确定，剩下的
        # print("waiting ",i)
        for j in range(len(alist)-i):
            # print("waited ",j) 
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
        print(alist)
    return alist

# myList=Bubble([2,2,2,2,2,2,1,-1,-1])
myList=Bubble([6,5,4,3,2,1])
# print(myList)
                