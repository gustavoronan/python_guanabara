#Criar uma tabuada com laço de repetição
tabuada = int(input("Digite um numero para ver sua tabuada: "))

for c in range (1,11):
   print("{} x {} = {}".format(tabuada, c, tabuada*c))
    
