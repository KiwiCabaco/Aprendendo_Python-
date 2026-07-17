# Calc (Short for calcultor)
continuar_programa = True

while continuar_programa:
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: digite um número válido.")

    while True:
        try:
            n2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: digite um número válido.")

    op = input("Digite a operação (+, -, *, /): ") 
    while op != "+" and op != "-" and op != "*" and op != "/":
        print("Erro: operação inválida.")
        op = input("Digite a operação (+, -, *, /): ")
    while True:
        try: 
            if op == "+":
                resultado = n1 + n2
            elif op == "-":
                resultado = n1 - n2
            elif op == "*":
                resultado = n1 * n2
            elif op == "/":
                resultado = n1 / n2
            print("Resultado:", resultado)
            break
        except ZeroDivisionError:
            print("Erro: não é possível dividir por zero.")
            break
    
    while True:
        continuar = input("Deseja fazer outro calcúlo? (s/n): ")
        if continuar == "n":
            continuar_programa = False
            break
        elif continuar != "s" and continuar != "n":
            print("Erro: Digite (s/n)!")
            continue
        else:
            break
            





