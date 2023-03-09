def diff(i,j,k,l):
    calc = i*j - k*l
    if calc < 0:
        return calc * -1
    return calc
    

pop_A = int(input())
taxa_crescimento_A = float(input())/100

pop_B = int(input())
taxa_crescimento_B = float(input())/100

print(diff(pop_A,taxa_crescimento_A,pop_B,taxa_crescimento_B))
