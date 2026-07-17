# GERENCIADOR DE COMPRAS

#1. Adicionar um item a uma lista de compras (nome do item + preço)
#2. Remover um item da lista (pelo nome)
#3. Listar todos os itens, mostrando também o total a pagar
#4. Sair do programa

lista_compras = {}

while True:
    print("--- MENU ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Listar itens")
    print("4. Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Nome do item: ")
        preco = float(input("Preço: "))
        lista_compras[nome] = preco
        print("Item adicionado!")
    elif opcao == 2:
        remover = input("Digite o item que deseja remover: ")
        for item in lista_compras:
            if item == remover:
                del lista_compras[remover]
                print("Item removido!")
                break
            else:
                print("Esse item não está na lista de compras.")
                break
    elif opcao == 3:
        print("Itens da lista:")
        total = 0
        for chave, valor in lista_compras.items():
            print(f"- {chave}: R$ {valor}")
            total += valor
        print(f"Total: R$ {total}")
        
    elif opcao == 4:
        break



