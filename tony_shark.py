# Enter your code here. Read input from STDIN. Print output to STDOUTn=int(raw_input())
n=int(raw_input())
d_fin=[]
p_fin=[]

tale_count1=1
tale_count2=2
for i in range(n):
    line1 = ' '*(n*n-i) + 'M'*(2*i+1) + ' '*(2*n*(n+3)-(n*n+i+1)-n) + ' '*(2*n-i-1) + 'M'*(tale_count1//2)
    d_fin.append(line1)
    
    line2 = ' '*(n*n-i) + 'M'*(2*i+1) + ' '*(2*n*(n+3)-(n*n+i+1)-n) + ' '*(2*n-i-2) + 'M'*(tale_count2//2)
    p_fin.append(line2)
    
    tale_count1+=1
    tale_count2+=1
    
body=[]


tale_count=2*n
for j in range(n+1):
    line=' '*(n-2)*j + 'M'*(2*n*(n+3)-2*n*j) + ' '*(2*n*(n+3)-((n-2)*j+2*n*(n+3)-2*n*j)-n) + ' '*(j-1) 
    if j!=0:
        line=line +  'M'*(tale_count//2)
        tale_count-=1
    body.append(line)
    


    
for z in d_fin:
    print z

body.reverse()
for y in body:
    print y

body.pop()
body.reverse()
for x in body:
    print x


p_fin.pop()
p_fin.reverse()
for w in p_fin:
    print w
