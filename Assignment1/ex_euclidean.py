# Extended Euclidean

a = [56211,43159,53947,19385]
for i in range(2):
    s=0
    olds=1
    t=1
    oldt=0
    r=a[i+2]
    oldr=a[i]
    while(r!=0):
        q=oldr//r
        t1=r
        r=oldr-(q*r)
        oldr=t1
        t1=s
        s=olds-(q*s)
        olds=t1
        t1=t
        t=oldt-(q*t)
        oldt=t1
    print(oldt)