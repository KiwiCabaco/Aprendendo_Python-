lista = []

print("Digite os numeros um de cada vez. Digite 'fim' para parar.")
while True:
    numero = input("Número: ")
    if numero == "fim":
        break
    else:
        lista.append(float(numero))

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

def calcular_maior(lista):
    maior_numero = lista[0]
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

def calcular_menor(lista):
    menor_numero = lista[0]
    for numero in lista:
        if numero < menor_numero:
            menor_numero = numero
    return menor_numero

def calcular_pares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
    return pares

def filtrar_maiores_que(lista, valor):
    lista_filtrada = []
    for numero in lista:
        if valor < numero:
            lista_filtrada.append(numero)
    return lista_filtrada


while True:
    print("\n--- MENU ---")
    print("1. Calcular média")
    print("2. Calcular maior")
    print("3. Calcular menor")
    print("4. Contar pares")
    print("5. Flitrar maiores que valor")
    print("6. Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um valor válido.")

    if opcao == 1:
        print("A média é:", calcular_media(lista))
    elif opcao == 2:
        print("O maior número é:", calcular_maior(lista))
    elif opcao == 3:
        print("O menor número é:", calcular_menor(lista))
    elif opcao == 4:
        print("A quantidade de números pares é:", calcular_pares(lista))
    elif opcao == 5:
        filtrador = float(input("Qual deve ser usado para a filtração: "))
        print("Lista Filtrada:", filtrar_maiores_que(lista, filtrador))
    elif opcao == 6:
        break
