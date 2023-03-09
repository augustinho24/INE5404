numeros = []
numeros_impares = []

for i in range(50):
    numeros.append(i)

for num in numeros:
    if num % 2 != 0:
        numeros_impares.append(num) 

print(*numeros_impares)        
