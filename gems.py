n=int(raw_input())
L1=map(int,raw_input().split())

L2=L1[:]

while(True):
    total=0
    L2=L1[:]
    for i in L1:
        count=(L1.count(i))
        if(L1.count(i)<2):
            total+=1
            L2.ao
        else:
            for j in range(count//2):
                L2.remove(i)
                L2.remove(i)
                L2.append(i+1)
        L1=L2[:]
    if(len(L1)==total):
        break

print len(L2)
