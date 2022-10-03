class BigTopHeap():
    def __init__(self,mylist:list):
        self.mylist=mylist
        self.mark=1
        while self.mark==1:
            self.build()

    def build(self):
        self.mark=0
        n=len(self.mylist)-1
        for  i  in range(n):
            if 2*i+2<=n:#左右子树都存在
                self.cmp(i,i*2+1,i*2+2)
            elif 2*i+1<=n:#只存在左子树
                # self.cmp(i,i*2+1)
                if self.mylist[i]<self.mylist[2*i+1]:
                    self.swap(i,2*i+1)
            else:
                break

    def cmp(self,head,left,right):
        if self.mylist[head]<self.mylist[left]:
            print("要调换head left" +str(head)+"---"+str(left))
            self.swap(head,left)

        if self.mylist[head]<self.mylist[right]:
            print("要调换head right" +str(head)+"---"+str(right))
            self.swap(head,right)
    def swap(self,n1,n2):
        self.mark = 1
        self.mylist[n1],self.mylist[n2]=self.mylist[n2],self.mylist[n1]
        print(self.mylist)
    def show(self):
        return self.mylist
alist=BigTopHeap([1,2,3,4,7,9,8,6])
print(alist.show())


