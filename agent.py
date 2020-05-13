t=int(raw_input())

L=[]
for a in range(t):
    n=int(raw_input())
    temp=[]
    for b in range(n):
        temp.append(int(raw_input()))
    L.append(temp)


for c in L:
    print(max(c)-len(c)+1)
