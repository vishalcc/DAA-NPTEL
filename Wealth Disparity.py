from itertools import combinations
class Emp:
    def __init__(self,name,wealth):
       self.name=name
       self.wealth=wealth
       self.emps=list()
       self.color='black'
    def add_emp(self,name):
        self.emps.append(name)
        self.emps.sort()

class DFS:
    vertex={}
    king=0
    def add_vertex(self,emp):
        if(isinstance(emp,Emp)):
            self.vertex[emp.name]=emp
    def add_edge(self,u,v):
        if(v==-1):
            self.king=u
        elif(u not in self.vertex[v].emps):
            self.vertex[v].emps.append(u)
    def print_dsf(self):
        for key,val in self.vertex.items():
            print('Index :',key,'Value :',val.emps)
    max=0
    def maxDiff(self,l1,l2,max):
        if((self.vertex[l1].wealth-self.vertex[l2].wealth)>max):
            self.max=self.vertex[l1].wealth-self.vertex[l2].wealth
        return self.max
    def callMaxDiff(self,i):
        li=list(combinations(i,2))
        for i in li:
            self.max=self.maxDiff(i[0],i[1],self.max)
        return self.max

    stack = []
    def stacks(self):
        self.stack.append(self.king)
        abc=[]
        while (len(self.vertex[self.king].emps) > 0):
            u = self.vertex[self.king].emps.pop(0)
            self.stack.append(u)
            n = 0

            while (n == 0 and len(self.stack)>0 and len(self.vertex[self.stack[-1]].emps) >= 0):
                if (len(self.vertex[self.stack[-1]].emps) == 0):
                    self.max=self.callMaxDiff(self.stack)
                    while (len(self.stack)>0 and len(self.vertex[self.stack[-1]].emps) == 0):
                        self.stack.pop()
                        if (len(self.stack) == 0):
                            n = 1
                            break
                else:
                    z = self.stack[-1]
                    self.stack.append(self.vertex[z].emps.pop(0))
        print(self.max)



g=DFS()
#li=[x for x in range(1,int(input())+1)]
#wealths=list(map(int,input().split(' ')))
#parent=list(map(int,input().split(' ')))
#for i,j in zip(li,wealths):
#    g.add_vertex(Emp(i,j))
#for i,j in zip(li,parent):
#    g.add_edge(i,j)

li=[x for x in range(1,5)]
wealths=[5,10,6,12]
parent=[2,-1,4,2]
for i,j in zip(li,wealths):
    g.add_vertex(Emp(i,j))
for i,j in zip(li,parent):
    g.add_edge(i,j)

g.print_dsf()
g.stacks()

