class Bebida:  #Programa Escolher Bebidas - João Andrade
    def __init__(self):
        self.sabores = {"Café": 0, "Chá": 0, "Chocolate Quente": 0, "Capuccino": 0, "Maté": 0}
        self.tamanhos = ["grande", "pequeno", "médio"]
    def escolher_bebida(self):
        while True:
            print("Bebidas disponíveis:", ", ".join(self.sabores.keys()))
            sabor = input("Escolha a bebida: ").title()
            if sabor in self.sabores:
                break
            print("Deve escolher 1 bebida da lista!")
        while True:
            print("Tamanhos disponíveis:", ", ".join(self.tamanhos))
            tamanho = input("Escolha o tamanho: ").lower()
            if tamanho in self.tamanhos:
                break
            print("Deve escolher 1 tamanho da lista!")
        temperatura = "Fria"
        aquecer = input("Deseja aquecer a bebida? (sim/não)|(quente/frio): ").lower()
        if aquecer in ["sim", "quente"]:
            print("A aquecer...")
            self.sabores[sabor] = 1
            temperatura = "Quente"
        print(f"Bebida escolhida: {sabor} ({tamanho.capitalize()}) - Temperatura: {temperatura}.")
bebida = Bebida()
bebida.escolher_bebida()