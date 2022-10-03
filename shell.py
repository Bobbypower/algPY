def ShellSort(alist):
    n=len(alist)
    k = n//2

    while k>0:
        for i in range(k,n):
            temp=alist[i]
            j=i
            while j >= k and alist[j-k] > temp:
                alist[j]=alist[j-k]
                j=j-k
                alist[j]=temp
        k = k//2
    return alist

print(ShellSort([2,3,4,5,9,8,7,6]))
print(ShellSort([1,2,3,4,5,7,8,9,0]))
print(ShellSort([2,2,2,2,2,2,1,1,1,3,3,-1]))


# 二叉平衡 哈夫曼 树
