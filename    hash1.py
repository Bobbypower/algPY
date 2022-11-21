MaxIndex=10
MaxNum=15

hashT2=[-1]*MaxNum
print(hashT2)




def cHashT(num,hashT):
    tmpI=num%MaxIndex
    while True:
        if hashT[tmpI] == -1:
            hashT[num%MaxIndex]==num
            return hashT
        else:
            tmpI=(num+1)%MaxIndex
cHashT(2,hashT2)
cHashT(5,hashT2)

cHashT(8,hashT2)
cHashT(9,hashT2)
cHashT(3,hashT2)
cHashT(6,hashT2)
cHashT(1,hashT2)


print(hashT2)


