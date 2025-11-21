def bc (n):
    
    
        n
        b=""
        while n>0:
            r=n%2
            b=str(r)+b
            n=n//2
        print (b)
        
def bn (n):
    x = (n*2)
    s =str (x)
    g= list(s)
    
    e=0
    h=0
    for i in range(len(g)-1,-1,-1):
        v=int(g.pop(i))
        
        h+=(v**e)
        e+=1
    print (h)
def bcc (f):
        c=0
        while c <= f:
                bc(c)
                c = c+1
