#LER A MEDIA

nota1 = float (input("Insira a primeira nota: "))
nota2 = float (input("Insira a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"Sua nota final foi {media}")
if media >= 7:
    print("Sua nota garante sua aprovação")
else:
    print("Reprovado")