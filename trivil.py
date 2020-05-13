while True:
    n=int(raw_input())

    x=n%52

    if(n<=26):
        print n
    elif(x==1):
        print 26
    elif(x<28):
        print 0
    else:
        print x-26
        
