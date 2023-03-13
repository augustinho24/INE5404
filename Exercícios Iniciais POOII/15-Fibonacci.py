def fibonacci(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1 
    else:

        a = 1
        b = 1
        for i in range(3, x+1):
         c = a + b
         a = b
         b = c
         print(c)


n = int(input("Digite um número: "))
fibonacci(n)

   

