#Union a list
from random import randint
l1=[randint(1,10) for x in range(int(input()))]
l2=[randint(1,10) for x in range(int(input()))]
union=[]
leng=len(l1) if len(l1)>len(l2) else len(l2)
print(l1,l2)
for i in range(leng):
    if(i<len(l1)):
        if(l1[i] not in union):
            union.append(l1[i])
    if (i < len(l2)):
        if (l2[i] not in union):
            union.append(l2[i])

print(union)