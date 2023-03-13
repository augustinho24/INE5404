
n = [int(x) for x in input().split()]

while any (x < 0 or x > 1000 for x in n):
    print("Erro")
    n = [int(x) for x in input("Insira novamente: ").split()] 
       
print(f"Menor: {min(n)}")
print(f"Maior: {max(n)}")
print(f"Soma: {sum(n)}")
