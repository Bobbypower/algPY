def myShell(alist):
    n=len(alist)
    k=n//2
    while k>0:
        print("k=",k)
        for i  in range(k,n):
            print("i=",i)
            for j in  range(i,k-1,-k):
                
                
                if alist[j]<alist[j-k]:
                    print("j=",j)
                    print("j-k=",j-k)
                    alist[j-k],alist[j]=alist[j],alist[j-k]
                    print(alist)
                else:
                    break
        k //=2
    return alist

myList=myShell([7,6,5,4,3,2,1])
# print(myList)