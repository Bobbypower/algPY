def shiftup(alist,low,high):
    i = low
    j = 2*i+1
    tmp=alist[i]
    while j <= high:
        if j < high and alist[j] < alist[j+1]:
            j=j+1
        if tmp<alist[j]:
            alist[i]=alist[j]
            i=j
            j=2*i+1

        else:
            alist[i] = tmp
            break
    else:
        alist[i] = tmp

def heap_sort(alist):

    n= len(alist)
    for i  in range((n-2)//2,-1,-1):
        shiftup(alist,i,n-1)
    for i in range(n-1,-1,-1):
        alist[0],alist[i]=alist[i],alist[0]
        shiftup(alist,0,i-1)
    return  alist

print(heap_sort([2,6,8,4,9,134]))
