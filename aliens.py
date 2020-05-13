[n,m]=map(int,raw_input().rstrip().split())

S=range(1,n+1)


T=range(n+1,2*n+1)

S_road=[]

T_road=[]

answer=0

for i in range(m):
    x,y=map(int,raw_input().rstrip().split())
    
    if (x in S) and (y in S):
        continue
    
    elif (x in T) and (y in T):
        continue
    else:
        if x in S_road:
            if y in T_road:
                continue
        elif x not in S_road:
            if y not in T_road:
                S_road.append(x)
                T_road.append(y)
                answer+=1
            else:
                continue
        
print answer
            
