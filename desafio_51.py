#Progressão aritimética

pr = int(input("Insira a progressão: "))
rz = int(input("Insira a razão: "))
decimo = pr + (10 - 1) * rz
for c in range (pr, decimo + rz, rz):
    print(c)