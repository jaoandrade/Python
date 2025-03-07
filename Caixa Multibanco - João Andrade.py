saldo = 1000    #Caixa Multibanco - João Andrade
while True:
    opcao = int(input("1: Consultar saldo.\n2: Depositar dinheiro.\n3: Retirar dinheiro.\n4: Sair.\nEscolha uma opção: "))
    match opcao:
        case 1:
            print("Seu saldo é: ",saldo," $")
        case 2:
            deposito = int(input("Quanto deseja depositar? "))
            if deposito > 0:
                saldo += deposito
                print("Depósito feito com sucesso. Novo saldo: ",saldo," $")
            else:
                print("Impossível fazer um depósito com valores negativos.")
        case 3:
            retirar = int(input("Quanto deseja retirar? "))
            if retirar > 0:
                if retirar <= saldo:
                    saldo -= retirar
                    print("Retirou com sucesso. Novo saldo: ",saldo," $")
                else:
                    print("Saldo insuficiente para a retirada.")
            else:
                print("Impossível retirar valores negativos.")
        case 4:
            print("Encerrando o programa.")
            break