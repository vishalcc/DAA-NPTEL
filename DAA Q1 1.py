import math
i,j,k=0,0,0
x,y=list(map(int,input().split(' ')))
for z in range(x,y+1):
    if(math.gcd(z,9381)>2):
        i=i+z
        k=k+z
    else:
        j=j+z
        k=k+z

print('i={} j={} k= {}'.format(i,j,k),i-j,j-i,i+j)