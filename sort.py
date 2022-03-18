import random 
import time

def insertion(ar):    
    for i in range(len(ar)):
        j=i-1
        ch=i
        while j>=0:
            if (ar[ch]<ar[j]):
                ar[ch],ar[j]=ar[j],ar[ch]
                ch=j
            j-=1
    return ar
            

def selection(ar):
    for i in range(len(ar)):
        pos=i
        for j in range(i+1,len(ar)):
            if(ar[pos]>ar[j]):
                pos=j
        ar[i],ar[pos]=ar[pos],ar[i]
    return ar



def quickSort(ar):          
    if len(ar)<=1:              
        return ar
    lf,rt=[],[]
    p=ar[0]
    for j in ar:
        if j>=p:
            rt.append(j)
        else:
            lf.append(j)
    l=quickSort(lf)
    r=quickSort(rt[1:])
    c=l+[rt[0]]+r
    '''for u in c:
        print(u)
    '''
    return c



def mergesort(ar):
    if len(ar)<=1:
        return ar
    middle=int(len(ar)/2)
    left=ar[:middle]
    right=ar[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    #print(res)
    return res
def merge(left,right):
    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res


ar = []
for i in range(1000000):
    ar.append(random.randint(1,20))

#ar = [2,7,6,11,89,41,32,45,67,]
arMerg=ar
arQuick=ar
arInsert=ar
arSelect=ar

basla=time.time()
ar1 = mergesort(arMerg)
print("merge sort:")
bitis=time.time()
#print(ar1)
print("saniye sürdü:"+ str((bitis-basla)))
print("-----------------")

basla1=time.time()
#ar2 = quickSort(arQuick)
print("quick sort:")
bitis1=time.time()
#print(ar2)
print("saniye sürdü:"+ str((bitis1-basla1)))
print("-----------------")

basla2=time.time()
ar3 = selection(arSelect)
print("selection sort:")
bitis2=time.time()
#print(ar3)
print("saniye sürdü:"+ str((bitis2-basla2)))
print("-----------------")

basla3=time.time()
ar4 = insertion(arInsert)
print("insertion sort:")
bitis3=time.time()
#print(ar4)
print("saniye sürdü:"+ str((bitis3-basla3)))
print("-----------------")
