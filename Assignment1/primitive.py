# Primitive elements

a = [39877,31319,39869]
for i in range(3):
    b=[1]
    for j in range(2,a[i]):
        if(a[i]%j!=0):
            b.append(j)
    print(b)      