class Veiculo:
    def __init__(self, modelo, marca, ano, consumo): #Programa de Frotas e Viagens - João Andrade e Julien Manolico
        self.modelo = modelo 
        self.marca = marca
        self.ano = ano
        self.consumo = consumo 
        self.deposito_combustivel = 0.0
    def abastecer(self, litros):
        if litros > 0:
            self.deposito_combustivel += litros
            print(f"Abasteceste com {litros} litros. Tanque atual: {self.deposito_combustivel} litros.")
        else:
            print("Quantidade de litros não pode ser negativa para abastecer.")
    def conduzir(self, distancia):
        if distancia <= 0:
            print("A distância não pode ser negativa.")
            return
        necessario = distancia / self.consumo 
        if necessario <= self.deposito_combustivel:
            self.deposito_combustivel -= necessario
            print(f"\nViagem de {distancia} km realizada. Combustível restante: {self.deposito_combustivel:.2f} litros.")
            input("Enter para continuar...")
        else:
            print("\nCombustível insuficiente para conduzir.")
            input("Enter para continuar...")
    def exibir_informacoes(self):
        print(f"\n===== Informações do Veículo =====\nModelo: {self.modelo}\nMarca: {self.marca}\nAno: {self.ano}\nConsumo: {self.consumo} km/l\nCombustível no tanque: {self.deposito_combustivel:.2f} litros\n==================================\n")
        input("Enter para continuar...")
class Frota:
    def __init__(self):
        self.veiculos = []
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        print(f"Veículo {veiculo.modelo} adicionado à frota.")
        input("Enter para continuar...")
    def listar_veiculos(self):
        if not self.veiculos:
            print("Nenhum veículo registrado na frota.")
        else:
            print("\nLista de veículos na frota:")
            for veiculo in self.veiculos:
                print(f"- {veiculo.modelo} ({veiculo.marca}, {veiculo.ano})")
        input("Enter para continuar...")
    def encontrar_veiculo(self, modelo):
        for veiculo in self.veiculos:
            if veiculo.modelo.lower() == modelo.lower():
                return veiculo
        print("\nVeículo não encontrado.")
        return None
    def usar_veiculo(self, modelo):
        veiculo = self.encontrar_veiculo(modelo)
        if veiculo:
            while True:
                print(f"\nUsando o veículo {veiculo.modelo}. Escolha uma opção:")
                print("1 - Abastecer\n2 - Conduzir\n3 - Exibir Informações\n4 - Parar de usar veículo")
                opcao = input("Opção: ")
                if opcao == "1":
                    litros = float(input("Quantos litros deseja abastecer? "))
                    veiculo.abastecer(litros)
                elif opcao == "2":
                    distancia = float(input("Qual a distância que deseja conduzir(km)? "))
                    veiculo.conduzir(distancia)
                elif opcao == "3":
                    veiculo.exibir_informacoes()
                elif opcao == "4":
                    print(f"Parando de usar o veículo {veiculo.modelo}.")
                    break
                else:
                    print("Opção inválida.")
def main():
    frota = Frota()
    while True:
        print("\nEscolha uma opção:\n1 - Adicionar Veículo\n2 - Listar Veículos\n3 - Informações Veículo\n4 - Usar Veículo\n5 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            marca = input("Diga a marca do veículo: ")
            modelo = input("Diga o modelo do veículo: ")
            ano = int(input("Diga o ano do veículo: "))
            consumo = float(input("Diga o consumo do veículo (km por litro): "))
            veiculo = Veiculo(modelo, marca, ano, consumo)
            frota.adicionar_veiculo(veiculo)
        elif opcao == "2":
            frota.listar_veiculos()
        elif opcao == "3":
            modelo = input("Diga o modelo do veículo que deseja as informações: ")
            veiculo = frota.encontrar_veiculo(modelo)
            if veiculo:
                veiculo.exibir_informacoes()
        elif opcao == "4":
            modelo = input("Diga o modelo do veículo que deseja usar: ")
            frota.usar_veiculo(modelo)
        elif opcao == "5":
            print("Fechando o programa...")
            break
        else:
            print("Opção inválida, escolha uma opção entre 1 e 5.")
if __name__ == "__main__":
    main()