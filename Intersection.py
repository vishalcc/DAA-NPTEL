from time import time
from random import randint
l1=[x+x for x in range(1000)]
l2=[x*x for x in range(1000)]
intersection=[]
big=l1 if(len(l1)>len(l2)) else l2
small=l1 if(len(l2)>len(l1)) else l1
t=time()
for i in small:
    if(i in intersection):
        pass
    else:
        for j in big:
            if(i==j):
                intersection.append(i)
                break
t1=time()
print('take time ',t1-t,t,t1)
t=time()
s1=set(small)
s2=set(big)
l3=list(s1.intersection(s2))
t1=time()
print('time taken by com',t1-t,t,t1)

