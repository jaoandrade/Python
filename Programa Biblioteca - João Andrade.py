class Biblioteca:     #Programa Biblioteca - João Andrade
    def __init__(self):
        self.livros = {}
    def adicionar_livro(self, titulo, autor, ano):
        if titulo in self.livros:
            print(f"O livro '{titulo}' já foi adicionado na biblioteca.")
        else:
            self.livros[titulo] = {"autor": autor, "ano": ano, "disponivel": 1}
            print(f"\nO Livro '{titulo}' foi adicionado.")
    def listar_disponiveis(self):
        print("\nLivros disponíveis:")
        disponiveis = [titulo for titulo, info in self.livros.items() if info["disponivel"] == 1]
        if disponiveis:
            for titulo in disponiveis:
                info = self.livros[titulo]
                print(f"- {titulo} | Autor: {info['autor']} | Ano: {info['ano']}")
        else:
            print("Nenhum livro disponível no momento.")
    def listar_emprestados(self):
        print("\nLivros emprestados:")
        emprestados = [titulo for titulo, info in self.livros.items() if info["disponivel"] == 0]
        if emprestados:
            for titulo in emprestados:
                info = self.livros[titulo]
                print(f"- {titulo} | Autor: {info['autor']} | Ano: {info['ano']}")
        else:
            print("Nenhum livro emprestado no momento.")
    def emprestar_livro(self, titulo):
        if titulo in self.livros:
            if self.livros[titulo]["disponivel"] == 1:
                self.livros[titulo]["disponivel"] = 0
                print(f"Livro '{titulo}' foi emprestado com sucesso.")
            else:
                print(f"Livro '{titulo}' já está emprestado.")
        else:
            print(f"Livro '{titulo}' não encontrado na biblioteca.")
    def devolver_livro(self, titulo):
        if titulo in self.livros:
            if self.livros[titulo]["disponivel"] == 0:
                self.livros[titulo]["disponivel"] = 1
                print(f"Livro '{titulo}' devolvido com sucesso.")
            else:
                print(f"Livro '{titulo}' já estava disponível.")
        else:
            print(f"Livro '{titulo}' não encontrado na biblioteca.")
    def remover_livro(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo]
            print(f"Livro '{titulo}' foi removido da biblioteca.")
        else:
            print(f"Livro '{titulo}' não foi encontrado na biblioteca.")
biblioteca = Biblioteca()
while True:
    print("\nBiblioteca || João Andrade\n1 - Adicionar um livro\n2 - Remover um livro da biblioteca\n3 - Listar livros disponíveis\n4 - Listar livros emprestados\n5 - Emprestar um livro\n6 - Devolver um livro\n0 - Sair")
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            titulo = input("Diga o título do livro: ")
            autor = input("Diga o autor do livro: ")
            ano = input("Diga o ano de publicação: ")
            biblioteca.adicionar_livro(titulo, autor, ano)
            input("\nPressione Enter para continuar...")
        case "2":
            titulo = input("Diga o título do livro para remover da biblioteca: ")
            biblioteca.remover_livro(titulo)
            input("\nPressione Enter para continuar...")
        case "3":
            biblioteca.listar_disponiveis()
            input("\nPressione Enter para continuar...")
        case "4":
            biblioteca.listar_emprestados()
            input("\nPressione Enter para continuar...")
        case "5":
            titulo = input("Diga o título do livro para emprestar: ")
            biblioteca.emprestar_livro(titulo)
            input("\nPressione Enter para continuar...")
        case "6":
            titulo = input("Diga o título do livro para devolver: ")
            biblioteca.devolver_livro(titulo)
            input("\nPressione Enter para continuar...")
        case "0":
            print("A encerrar programa, até a próxima...")
            break
        case _:
            print("Opção inválida..")