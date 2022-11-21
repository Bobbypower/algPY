# Created on 刘已乐的iPad.

# print ('Hello World!')

def QuickSort(alist):
    # print(alist)    
    n=len(alist)
    # blist=[]
    if len(alist) <= 1:
        return alist
    else:
        left=[]
        right=[]
        print(alist)
        pivot=alist[n//2]
        alist.remove(pivot)
        # print(alist)
        for  num  in  alist:
            if num  >=  pivot:
                right.append(num)
                print(right)
            else:
                left.append(num)
                print(left)
        return QuickSort(left)+[pivot]+QuickSort(right)

        
print(QuickSort([7,6,5,3,3,3,2,2,1]))