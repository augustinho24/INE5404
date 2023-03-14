
A = 80000
B = 200000
anos = 0
while True:
    anos +=1
    A += A*0.03
    B += A*0.015
    if A > B:
        break

print(anos)



