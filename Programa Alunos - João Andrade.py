class Aluno:  #Programa Alunos - João Andrade
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    def calcular_media(self):
        total = 0
        for nota in self.notas:
            total += nota
        return total / len(self.notas)
    def obter_status(self):
        return "Aprovado" if self.calcular_media() >= 7 else "Reprovado"
def registar_aluno():
    nome = input("Nome do aluno: ")
    idade = int(input("Idade do aluno: "))
    notas = []
    num_notas = int(input("Quantas notas deseja inserir? "))
    for _ in range(num_notas):
        while True:
            nota = float(input("Digite uma nota (0 a 20): "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("As notas devem entre 0 e 20 valores.")
    return Aluno(nome, idade, notas)
def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno registado.")
        return
    print("\nLista de alunos:")
    for aluno in alunos:
        print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, Média: {aluno.calcular_media():.2f}, Status: {aluno.obter_status()}")
def main():
    alunos = []
    while len(alunos) < 5:
        print("\n1. Registar aluno\n2. Listar alunos\n3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            alunos.append(registar_aluno())
            if len(alunos) == 5:
                print("Turma Completa")
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            break
        else:
            print("Opção Inválida.")
if __name__ == "__main__":
    main()