preço = 0   #Lojinha - João Andrade
carrinho = []
produtos = {'camisa': 15, 't-shirt': 10, 'calças': 25, 'casaco': 50}
while True:
    opção = input("==== Lojinha ====\nOpções: Comprar | Remover | Carrinho | Finalizar(Comprar)/Sair\n1. T-Shirt - 10$\n2. Camisa - 15$\n3. Calças - 25$\n4. Casaco - 50$\nOpção: ")
    match opção:
        case 'Comprar' | 'comprar':
            item = input("O que deseja comprar?\n").lower()
            quantidade = int(input("Quantos deseja comprar?\n"))
            for i in range (quantidade):
             if item in produtos: 
                 carrinho.append(item)
                 preço += produtos[item]
             else:
                print("Produto não encontrado.")
                continue 
            if item in produtos:
                print(item,"adicionado ao carrinho!")
        case 'Remover' | 'remover':
            if not carrinho:
                print("Seu carrinho está vazio.")
            else:
                print(carrinho)
                item = input("Qual item deseja remover?\n").lower()
                quantidade = int(input("Quantos deseja remover?\n"))
                for i in range (quantidade):
                 if item in carrinho:
                     carrinho.remove(item)
                     preço -= produtos[item]
                 else:
                     print("Item não está no carrinho.")
                     continue
                if item in carrinho:
                    print(item,"removido do carrinho.")
        case 'Carrinho' | 'carrinho':
            print("\nPreço total:",preço,"$\nTotal de itens:",len(carrinho),"\nItens no carrinho:", carrinho if carrinho else "Carrinho vazio.")
            k = input("Escreva 'sair' para continuar..\n")
            if k == 'sair' or 'continuar':
                continue
        case 'Sair' | 'sair' | 'finalizar' | 'Finalizar':
            print("\nTotal Pago:",preço,"$\nTotal de itens:",len(carrinho),"\nItens no carrinho:", carrinho if carrinho else "Carrinho vazio.\nObrigado por visitar a lojinha!")
            break  