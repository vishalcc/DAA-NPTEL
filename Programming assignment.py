valid={}
srt,data=[],{'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,
             'm':6,'n':6,'o':6,'p':7,'q':7,'r':7,'s':7,'t':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9}
def mapfun(l):
    strs=''
    for i in l:
        strs+=str(data.get(i))

    return strs
for i in range(int(input())):
    lists=mapfun(input())
    valid[lists]=valid.get(lists,0)+1

maxs=max(list(valid.values()))
for i in valid:
    if(maxs==valid.get(i)):
        print(i)
        break