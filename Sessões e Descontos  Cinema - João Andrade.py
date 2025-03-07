idade = int(input("Diga sua idade: ")) #Sessões e Descontos | Cinema - João Andrade
if idade < 12:
    print("A sessão de cinema só é permitida a maiores de 12 anos.")
    exit()
preço = 15
opcao = input("Diga onde deseja sentar.\nP - Plateia\nB - 1º Balcão\nS - Balcão Superior\n").capitalize()
match opcao:
      case "P" | "p":
        print("O preço para o lugar fica de,",preço," euros.")
      case "B" | "b":
            print("O preço para o lugar fica de,",(preço*0.20)+preço," euros. Com um desconto já aplicado de 20%.")
      case "S" | "s":
          print("O preço para o lugar fica de,",(preço*0.30)+preço," euros. Com um desconto já aplicado de 30%.")