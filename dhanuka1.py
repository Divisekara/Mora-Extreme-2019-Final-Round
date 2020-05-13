[n,m]=map(int,raw_input().rstrip().split())
S=range(1,n+1)
T=range(n+1,2*n+1)
roadsS=[]
roadsT=[]
counts=0
for i in range(m):
    x,y=map(int,raw_input().rstrip().split())
    if (x in S) and (y in S):
        continue
    elif (x in T) and (y in T):
        continue
    else:
        if x in roadsS:
            if y in roadsT:
                continue
        elif x not in roadsS:
            if y not in roadsT:
                roadsS.append(x)
                roadsT.append(y)
                counts+=1
            else:
                continue
        
print counts
            
