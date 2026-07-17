
continuar = "s"

while continuar == "s":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    print("Sua média é:", media)

    if media >= 7:
        print("Aprovado")
    elif media <= 6.9 and media >= 5:
        print("Recuperação")
    else: 
        print("Reprovado")
    continuar = input("Deseja calcular a média de outro aluno? (s/n): ").lower()

print("Fim.")
