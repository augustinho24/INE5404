def exponenciacao (x,y):
    k = x
    for i in range (1,y):
        k = k*x
    return k
    
b, e = [int(x) for x in input().split()]

print(exponenciacao(b,e))

