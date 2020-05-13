# Enter your code here. Read input from STDIN. Print output to STDOUT
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm


L1=map(int,raw_input().split(","))

n=L1[0]
m=L1[1]
k=L1[2]
q=L1[3]

LCM=lcm(lcm(n,m),k)

L2=[]

for i in range(q):
    L2.append(map(int,raw_input().split(",")))

bamma=1

for a in range(1,min(n,m,k)+1):
    if (n%a==0 and m%a==0 and k%a==0):
        bamma=a

parathara=LCM/bamma

answer=[]

for b in L2:
    if (bamma==1):
        answer.append("YES")
    else:
        x1=b[0]
        y1=b[1]
        x2=b[2]
        y2=b[3]

        if (x1==1):
            y1=y1*(LCM/n)
        elif(x1==2):
            y1=y1*(LCM/m)
        else:
            y1=y1*(LCM/k)

        if (x2==1):
            y2=y2*(LCM/n)
        elif(x2==2):
            y2=y2*(LCM/m)
        else:
            y2=y2*(LCM/k)
            
        if(abs(y1-y2)>parathara):
            answer.append("NO")
        else:      
           for d in range(0,LCM,parathara):
               #print d,y1,y2
               if(y1==y2):
                   answer.append("YES")
                   break
                  
               if (y1<=d and y2<=d):
                   answer.append("YES")
                   break
                  
               elif(y1<d and y2>d):
                   answer.append("NO")
                   break
                  
               elif(y1>d and y2<d):

                   answer.append("NO")
                   break
           else:
               answer.append("NO")

#     if (abs(y1-y2)<parathara):
#         for d in range(1,LCM,parathara):
#             print d,y1,y2
#             if (abs(y1-d)>parathara or abs(y2-d)>parathara):
#                 gunithaya=(y1-d)*(y2-d)
#                 if (gunithaya>0):
#                    answer.append("YES")
#                 else:
#                     answer.append("NO")
         
#     else:
#         answer.append("NO")

for c in answer:
    print c
