class Bolo: #Programa de Bolos - João Andrade
    sabores = {"chocolate": 0, "baunilha": 0, "cenoura": 0, "morango": 0, "fuba": 0}
    ingredientes = ["ovos", "farinha", "açúcar", "raspa de limão", "pasta de açúcar", "cenoura", "morango", "óleo", "leite", "iogurte", "corante alimentar", "queijo"]
    tamanhos = ["grande", "pequeno", "medio", "médio"]

def mostrar_receita(sabor, ingredientes):
    print(f"Receita do bolo de {sabor}:")
    print("Ingredientes:", ", ".join(ingredientes))

def preparar_bolo(sabor, ingredientes, tamanho):
    Bolo.sabores[sabor] = 1
    print(f"O seu bolo de {sabor} com {', '.join(ingredientes[:-1])} e {ingredientes[-1]} está pronto. O tamanho escolhido foi {tamanho}. Bom Apetite!")
    exit()

def mostrar_status(sabor):
    if Bolo.sabores[sabor] == 1:
        print("O bolo está pronto!")
    else:
        print("Bolo por finalizar.")

def refazer_bolo():
    print("Refazendo e recomeçando a receita.")
    criar_bolo()

def criar_bolo():
    print("Sabores disponíveis:", ", ".join(Bolo.sabores.keys()))
    
    while True:
        sabor = input("Escolha o sabor do bolo: ").lower()
        if sabor in Bolo.sabores:
            break
        print("Sabor indisponível.")
    while True:
        tamanho = input("Escolha o tamanho do bolo (grande, médio, pequeno): ").lower()
        if tamanho in Bolo.tamanhos:
            break
        print("Tamanho não permitido.")
    print("Ingredientes disponíveis:", ", ".join(Bolo.ingredientes))
    ingredientes_escolhidos = []
    while len(ingredientes_escolhidos) < 5:
        ingrediente = input(f"Escolha um ingrediente ({len(ingredientes_escolhidos) + 1}/5): ").lower()
        if ingrediente not in Bolo.ingredientes:
            print("O ingrediente escolhido não está disponível.")
        elif ingrediente in ingredientes_escolhidos:
            print("Esse ingrediente já foi escolhido. Escolha outro.")
        else:
            ingredientes_escolhidos.append(ingrediente)
    while True:
        finalizar = input("Deseja finalizar o bolo? (sim/não): ").lower()
        if finalizar == "sim":
            preparar_bolo(sabor, ingredientes_escolhidos, tamanho)
            return 
        elif finalizar == "não":
            print("Bolo por finalizar.")
        else:
            print("Resposta inválida. Digite 'sim' ou 'não'.")  
        while True:
            acao = input("Escolha uma ação: mostrar_receita, preparar_bolo, mostrar_status, refazer_bolo, ou sair: ").lower()
            if acao == "mostrar_receita":
                mostrar_receita(sabor, ingredientes_escolhidos)
            elif acao == "preparar_bolo":
                preparar_bolo(sabor, ingredientes_escolhidos, tamanho)
                return  
            elif acao == "mostrar_status":
                mostrar_status(sabor)
            elif acao == "refazer_bolo":
                refazer_bolo()
            elif acao == "sair":
                return
            else:
                print("ação inválida")
criar_bolo()
