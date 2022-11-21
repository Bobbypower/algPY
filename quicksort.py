# from turtle import right



def QuickSort(alist):
    if len(alist) >= 2:
        left=[]
        right=[]
        pivot=alist[len(alist) // 2]
        alist.remove(pivot)
        for num in alist:
            if num >= pivot:
                right.append(num)
            else:
                left.append(num)
        return QuickSort(left)+[pivot]+QuickSort(right)
    else:
        return alist

print(QuickSort([5,83,67,9,20,20,20,20,20]))




