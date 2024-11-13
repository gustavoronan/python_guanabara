

primeiro = int(input("Insira o primeiro termo: ")) #recebe o termo
razao = int(input("Insira a razão: ")) #recebe a razap
termo = primeiro
count = 1 #contador inicia em um, vai auxiliar para mostrar os 10 termos solicitados
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while count <= total: #enquanto contador for menor igual a 10
        print(f"{termo}", end=' ')
        termo += razao
        count += 1
    print("pausa")
    mais = int(input("Quantos termos devem aparecer a mais? ")) #esta vareavel vai receber quantos termos a mais deve ser mostrado
print("Final")