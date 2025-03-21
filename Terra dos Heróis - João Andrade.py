import os
import random                                   # Terra dos Heróis - João Andrade
def limpar_ecrã():
    os.system("cls" if os.name == "nt" else "clear")
def menu_inicial():
    limpar_ecrã()
    print(r"""
╔══════════════════════════════════════════════╗
║        BEM-VINDO À TERRA DOS HERÓIS          ║
║       Onde lendas se forjam em batalha       ║
║         E o destino é forjado em ouro        ║
╚══════════════════════════════════════════════╝
                  Créditos: João Andrade

        [1] INICIAR AVENTURA
        [2] SAIR
    """)
    return input("\nEscolha uma opção: ")
def escolher_classe():
    print("\nEscolha a sua classe:")
    classes = ["1 - Guerreiro 🗡️", "2 - Mago 🔮", "3 - Arqueiro 🏹", "4 - Ladino 🗡️", "5 - Clérigo ✨"]
    for c in classes:
        print(c)
    while True:
        escolha = input("Número da classe escolhida: ")
        match escolha:
            case "1": return "Guerreiro"
            case "2": return "Mago"
            case "3": return "Arqueiro"
            case "4": return "Ladino"
            case "5": return "Clérigo"
            case _: print("Classe inválida. Tente novamente.")
def escolher_raca():
    print("\nEscolha a sua raça:")
    racas = ["1 - Humano 🧑", "2 - Elfo 🧝", "3 - Anão 🔨", "4 - Orc 💪", "5 - Meio-Demónio 👹"]
    for r in racas:
        print(r)
    while True:
        escolha = input("Número da raça escolhida: ")
        match escolha:
            case "1": return "Humano"
            case "2": return "Elfo"
            case "3": return "Anão"
            case "4": return "Orc"
            case "5": return "Meio-Demónio"
            case _: print("Raça inválida. Tente novamente.")
class Jogador:
    def __init__(self, nome, idade, genero, classe, raca):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.classe = classe
        self.raca = raca
        self.nivel = 1
        self.experiencia = 0
        self.fome = 0       
        self.sono = 0        
        self.vida = 100    
        self.gold = 50    
        self.inventario = [] 
        self.equipamentos = []
        self.last_work_level = 0  

    def ganhar_xp(self, valor):
        nivel_antigo = self.nivel
        self.experiencia += valor
        while self.experiencia >= 100 and self.nivel < 100:
            self.nivel += 1
            self.experiencia -= 100
        if self.nivel > nivel_antigo:
            print(f"\n{self.nome} subiu {self.nivel - nivel_antigo} nível(s)!")
            self.last_work_level = nivel_antigo  
            if self.nivel >= 100:
                print(f"\nParabéns, {self.nome}! Atingiu o nível máximo (100) e terminou a sua jornada!")
                input("Prima Enter para voltar ao menu...")

    def exibir_status(self):
        print(f"""
==== ESTADO DO JOGADOR ===
Nome: {self.nome}
Raça: {self.raca}
Classe: {self.classe}
Idade: {self.idade}
Género: {self.genero}
Nível: {self.nivel}
Experiência: {self.experiencia}
Vida: {self.vida}/100
Fome: {self.fome}/100
Sono: {self.sono}/100
Ouro: {self.gold} $
Inventário: {', '.join(self.inventario) if self.inventario else 'Vazio'}
Equipamentos: {', '.join(self.equipamentos) if self.equipamentos else 'Nenhum'}
============================
""")
        input("Prima Enter para continuar...")

def trabalhar(jogador):
    if jogador.last_work_level < jogador.nivel:
        ouro_trabalho = int(random.randint(25, 100) * 0.7)
        jogador.gold += ouro_trabalho
        jogador.last_work_level = jogador.nivel
        print(f"\nTrabalhou arduamente e ganhou {ouro_trabalho} de ouro!")
    else:
        print("\nO personagem está demasiado ocupado para trabalhar (só se pode trabalhar uma vez por nível)!")
    input("Prima Enter para continuar...")

def aventura_simples(jogador):
    if jogador.fome >= 80 or jogador.sono >= 80:
        print("\nEstá demasiado faminto ou cansado para se aventurar! Cuide-se primeiro!")
        input("Prima Enter para continuar...")
        return True

    print("\nPartiu para mais uma aventura...")
    if jogador.nivel < 5:
        xp_max = 60
    elif jogador.nivel < 20:
        xp_max = 100
    else:
        xp_max = 150

    resultado = random.randint(10, xp_max)
    failure_chance = max(0.2, 0.4 - (jogador.nivel * 0.003))
    if "Arma de classe" in jogador.equipamentos:
        failure_chance *= 0.85

    if random.random() < failure_chance:
        dano = random.randint(10, 30)
        if "Armadura de classe" in jogador.equipamentos:
            dano = int(dano / 1.3)
        jogador.vida -= dano
        print(f"A aventura falhou! {jogador.nome} foi ferido e perdeu {dano} de vida.")
    else:
        print(f"{jogador.nome} completou a aventura e ganhou {resultado} XP!")
        if "Arma de classe" in jogador.equipamentos:
            resultado = int(resultado * 1.3)
        jogador.ganhar_xp(resultado)
        chest_event_chance = 0.35
        if random.random() < chest_event_chance:
            if jogador.nivel < 5:
                pesos = {"pequeno": 0.7, "medio": 0.25, "grande": 0.05}
            elif jogador.nivel < 20:
                pesos = {"pequeno": 0.5, "medio": 0.35, "grande": 0.15}
            else:
                pesos = {"pequeno": 0.3, "medio": 0.4, "grande": 0.3}
            r = random.random()
            acumulador = 0
            tipo_bau = None
            for tipo, peso in pesos.items():
                acumulador += peso
                if r < acumulador:
                    tipo_bau = tipo
                    break
            if tipo_bau == "pequeno":
                ouro_encontrado = random.randint(10, 30)
                print(f"Encontrou um BAÚ PEQUENO numa ruína e ganhou {ouro_encontrado} de ouro!")
            elif tipo_bau == "medio":
                ouro_encontrado = random.randint(40, 60)
                print(f"Encontrou um BAÚ MÉDIO numa ruína e ganhou {ouro_encontrado} de ouro!")
            elif tipo_bau == "grande":
                ouro_encontrado = random.randint(80, 150)
                print(f"Encontrou um BAÚ GRANDE numa ruína e ganhou {ouro_encontrado} de ouro!")
            jogador.gold += ouro_encontrado
        else:
            if random.random() < 0.5:
                item = random.choices(
                    population=["Ração", "Poção de Vida", "Cristal de XP", "Artefato do Poder"],
                    weights=[0.45, 0.25, 0.25, 0.05],
                    k=1
                )[0]
                jogador.inventario.append(item)
                print(f"Encontrou um item: {item}!")
            else:
                print("Nada foi encontrado desta vez.")
    
    jogador.fome += int(resultado * 0.3)
    jogador.sono += int(resultado * 0.25)
    if jogador.vida <= 0:
        print("\nA sua vida chegou a zero. Morreu heroicamente...")
        input("Prima Enter para voltar ao menu inicial...")
        return False
    input("Prima Enter para continuar...")
    return True

def jornada_do_heroi(jogador):
    if jogador.fome >= 80 or jogador.sono >= 80:
        print("\nO herói precisa recuperar suas forças antes de prosseguir jornada!")
        input("Prima Enter para continuar...")
        return True

    if jogador.classe == "Guerreiro":
        required_weapon = "Arma de classe"
    elif jogador.classe == "Mago":
        required_weapon = "Bastão Mágico"
    elif jogador.classe == "Arqueiro":
        required_weapon = "Arco de Caça"
    elif jogador.classe == "Ladino":
        required_weapon = "Adaga Afiada"
    elif jogador.classe == "Clérigo":
        required_weapon = "Martelo Sagrado"
    else:
        required_weapon = "Arma de classe"

    if jogador.nivel < 15 or required_weapon not in jogador.equipamentos or "Armadura de classe" not in jogador.equipamentos:
        print("\nPara iniciar a Jornada do Herói é necessário ter a arma e a armadura de classe e estar no nível 15 ou superior!")
        input("Prima Enter para continuar...")
        return True

    reinos = ["Valéria", "Eldoria", "Drakonia", "Lumina", "Arcádia"]
    mensagens = [
        "Durante a jornada do herói, enfrentou demônios nas sombras...",
        "Durante a jornada do herói, salvou a capital!",
        f"Durante a jornada do herói, parou uma guerra em {random.choice(reinos)}!",
        "Durante a jornada do herói, enfrentou criaturas místicas!"
    ]
    print(random.choice(mensagens))

    resultado = random.randint(65, 220)
    failure_chance = max(0.2, 0.4 - (jogador.nivel * 0.003))
    if required_weapon in jogador.equipamentos:
        failure_chance *= 0.85

    if random.random() < failure_chance:
        dano = random.randint(10, 30) * 2
        if "Armadura de classe" in jogador.equipamentos:
            dano = int(dano / 1.3)
        jogador.vida -= dano
        print(f"Durante a jornada do herói, sofreu um golpe brutal e perdeu {dano} de vida!")
    else:
        print(f"Durante a jornada do herói, superou desafios épicos e ganhou {resultado} XP!")
        if required_weapon in jogador.equipamentos:
            resultado = int(resultado * 1.3)
        jogador.ganhar_xp(resultado)
        if random.random() < 0.1:
            if jogador.nivel < 5:
                pesos = {"pequeno": 0.7, "medio": 0.25, "grande": 0.05}
            elif jogador.nivel < 20:
                pesos = {"pequeno": 0.5, "medio": 0.35, "grande": 0.15}
            else:
                pesos = {"pequeno": 0.3, "medio": 0.4, "grande": 0.3}
            r = random.random()
            acumulador = 0
            tipo_bau = None
            for tipo, peso in pesos.items():
                acumulador += peso
                if r < acumulador:
                    tipo_bau = tipo
                    break
            if tipo_bau == "pequeno":
                ouro_encontrado = random.randint(10, 30)
                print(f"Encontrou um BAÚ PEQUENO e ganhou {ouro_encontrado} de ouro!")
            elif tipo_bau == "medio":
                ouro_encontrado = random.randint(40, 60)
                print(f"Encontrou um BAÚ MÉDIO e ganhou {ouro_encontrado} de ouro!")
            elif tipo_bau == "grande":
                ouro_encontrado = random.randint(80, 150)
                print(f"Encontrou um BAÚ GRANDE e ganhou {ouro_encontrado} de ouro!")
            jogador.gold += ouro_encontrado
        else:
            item = random.choices(
                population=["Artefato do Poder", "Poção de Vida", "Cristal de XP"],
                weights=[0.25, 0.375, 0.375],
                k=1
            )[0]
            jogador.inventario.append(item)
            print(f"Durante a jornada do herói, encontrou um item precioso: {item}!")
    
    jogador.fome += int(resultado * 0.3)
    jogador.sono += int(resultado * 0.25)
    if jogador.vida <= 0:
        print("\nA sua vida chegou a zero durante a jornada do herói. Morreu heroicamente...")
        input("Prima Enter para voltar ao menu inicial...")
        return False
    input("Prima Enter para continuar...")
    return True

def enfrentar_rei_demonio(jogador):
    if jogador.nivel < 50:
        print("\nVocê precisa estar no nível 50 para enfrentar o Rei Demônio!")
        input("Prima Enter para continuar...")
        return True

    decisao = input("\nVocê está prestes a enfrentar o Rei Demônio. Não há regresso. Deseja prosseguir? (S/N): ").strip().upper()
    if decisao != "S":
        print("Batalha cancelada. Retornando ao menu de aventuras...")
        input("Prima Enter para continuar...")
        return True

    print("\nVocê decidiu enfrentar o Rei Demônio!")
    print("Prepare-se para a batalha épica!")
    print(r"""
                             ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
""")
    boss_health = 400
    while boss_health > 0 and jogador.vida > 0:
        print(f"\nSua vida: {jogador.vida} | Vida do Rei Demônio: {boss_health}")
        print("Escolha sua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Esquivar")
        print("4 - Usar Poção de Vida (ação rápida; o boss não ataca nesta rodada)")
        acao = input("Sua escolha: ").strip()
        if acao == "1":
            damage = random.randint(15, 30)
            if (jogador.classe == "Guerreiro" and "Arma de classe" in jogador.equipamentos) or \
               (jogador.classe == "Mago" and "Bastão Mágico" in jogador.equipamentos) or \
               (jogador.classe == "Arqueiro" and "Arco de Caça" in jogador.equipamentos) or \
               (jogador.classe == "Ladino" and "Adaga Afiada" in jogador.equipamentos) or \
               (jogador.classe == "Clérigo" and "Martelo Sagrado" in jogador.equipamentos):
                damage = int(damage * 1.5)
            rnd = random.random()
            if rnd < 0.5:
                counter_damage = random.randint(20, 40)
                jogador.vida -= counter_damage
                print(f"O Rei Demônio atacou de volta e causou {counter_damage} de dano em você!")
            elif rnd < 0.8:
                damage = int(damage * 0.2)  
                print("O Rei Demônio defendeu e reduziu 80% do dano recebido!")
            else:
                boss_health = min(400, boss_health + 20)
                print("O Rei Demônio se recuperou e ganhou 20 de vida!")
            boss_health -= damage
            print(f"Você atacou e causou {damage} de dano ao Rei Demônio!")
        elif acao == "2":
            boss_damage = random.randint(20, 40)
            if random.random() < 0.7:
                boss_damage = int(boss_damage * 0.2)  
                print("Você defendeu com sucesso, reduzindo o dano recebido em 80%!")
            else:
                print("Sua defesa falhou!")
            jogador.vida -= boss_damage
            print(f"O Rei Demônio atacou e causou {boss_damage} de dano!")
        elif acao == "3":
            boss_damage = random.randint(20, 40)
            if random.random() < 0.4:
                boss_damage = 0
                print("Você esquivou com sucesso e não recebeu dano!")
            else:
                print("Você falhou em esquivar!")
            jogador.vida -= boss_damage
            print(f"O Rei Demônio atacou e causou {boss_damage} de dano!")
        elif acao == "4":
            if "Poção de Vida" in jogador.inventario:
                jogador.inventario.remove("Poção de Vida")
                heal = 30
                jogador.vida = min(100, jogador.vida + heal)
                print(f"Você usou uma Poção de Vida e recuperou {heal} pontos de vida!")
                print("Como ação rápida, o Rei Demônio não atacou nesta rodada.")
            else:
                print("Você não tem Poção de Vida!")
                continue
        else:
            print("Ação inválida!")
            continue

    if jogador.vida <= 0:
        print("\nVocê foi derrotado pelo Rei Demônio. Sua jornada termina aqui...")
        input("Prima Enter para voltar ao menu...")
        limpar_ecrã()
        menu_inicial()
    else:
        print(f"\nO Rei Demônio pereceu... a lenda do herói '{jogador.nome}' se eternizou! Que seus feitos inspirem gerações!\nAcumulaste uma riqueza de {jogador.gold} ouros.")
        print(r"""
         />_________________________________
[########[]_________________________________>
         \>
    """)
        input("Prima Enter para voltar ao menu...")
        limpar_ecrã()
        menu_inicial()

def menu_aventura(jogador):
    print("\n=== MENU DE AVENTURAS ===")
    print("1 - Aventura Simples")
    print("2 - Jornada do Herói")
    if jogador.nivel >= 50:
        print("3 - Enfrentar Rei Demônio")
    escolha = input("Escolha uma opção: ").strip()
    if escolha == "1":
        return aventura_simples(jogador)
    elif escolha == "2":
        return jornada_do_heroi(jogador)
    elif escolha == "3" and jogador.nivel >= 50:
        return enfrentar_rei_demonio(jogador)
    else:
        print("Opção inválida.")
        input("Prima Enter para continuar...")
        return True

def descansar(jogador):
    print("\n=== DESCANSAR ===")
    print("Escolha como quer descansar:")
    print("1 - Dormir na pousada (15 ouros, recupera muito sono, fome e vida)")
    print("2 - Dormir à fogueira (gratuito, recupera sono e metade da fome, não recupera vida)")
    opcao = input("Opção (1 ou 2): ").strip()

    if opcao == "1":
        custo_noite = 15
        if jogador.gold >= custo_noite:
            jogador.gold -= custo_noite
            print(f"Pagou {custo_noite} de ouro pela pousada.")
            recupera_sono = random.randint(40, 60)
            recupera_fome = random.randint(30, 50)
            recupera_vida = random.randint(30, 50)
        else:
            print("Ouro insuficiente. Dormirá à fogueira.")
            recupera_sono = random.randint(10, 20)
            recupera_fome = random.randint(10, 20)
            recupera_vida = 0
    elif opcao == "2":
        print("Optou por dormir à fogueira. É gratuito!")
        recupera_sono = random.randint(10, 20)
        recupera_fome = random.randint(10, 20)
        recupera_vida = 0
    else:
        print("Opção inválida. Dormirá à fogueira.")
        recupera_sono = random.randint(10, 20)
        recupera_fome = random.randint(10, 20)
        recupera_vida = 0

    jogador.sono = max(0, jogador.sono - recupera_sono)
    jogador.fome = max(0, jogador.fome - recupera_fome)
    jogador.vida = min(100, jogador.vida + recupera_vida)
    print("\nDescansou bem!")
    print(f"Sono reduzido: {recupera_sono}")
    print(f"Fome reduzida: {recupera_fome}")
    if recupera_vida:
        print(f"Vida recuperada: {recupera_vida}")
    input("Prima Enter para continuar...")

def usar_item(jogador):
    if not jogador.inventario:
        print("\nInventário vazio!")
        input("Prima Enter para continuar...")
        return

    print("\nItens disponíveis:")
    for idx, item in enumerate(jogador.inventario, 1):
        print(f"{idx} - {item}")
    try:
        idx = int(input("Escolha o número do item a usar: ")) - 1
        item = jogador.inventario.pop(idx)
        match item:
            case "Poção de Vida":
                jogador.vida = min(100, jogador.vida + 30)
                print("Vida recuperada!")
            case "Ração":
                jogador.fome = max(0, jogador.fome - 50)
                print("Fome reduzida!")
            case "Cristal de XP":
                xp = random.randint(30, 70)
                print(f"Cristal absorvido! Ganhou {xp} XP!")
                jogador.ganhar_xp(xp)
            case "Artefato do Poder":
                xp = random.randint(100, 200)
                print(f"Artefato liberou sua energia! Ganhou {xp} XP!")
                jogador.ganhar_xp(xp)
    except:
        print("Escolha inválida.")
    input("Prima Enter para continuar...")

def loja(jogador):
    if jogador.classe == "Guerreiro":
        arma_da_classe = "Arma de classe"
    elif jogador.classe == "Mago":
        arma_da_classe = "Bastão Mágico"
    elif jogador.classe == "Arqueiro":
        arma_da_classe = "Arco de Caça"
    elif jogador.classe == "Ladino":
        arma_da_classe = "Adaga Afiada"
    elif jogador.classe == "Clérigo":
        arma_da_classe = "Martelo Sagrado"
    else:
        arma_da_classe = "Arma de classe"
    
    itens_loja = {
        arma_da_classe: 200,
        "Armadura de classe": 100,
        "Poção de Vida": 25,
        "Ração": 20
    }
    print("\n=== LOJA DO AVENTUREIRO ===")
    lista_itens = list(itens_loja.items())
    for i, (item, preco) in enumerate(lista_itens, 1):
        print(f"{i} - {item}: {preco} ouro")
    print(f"Ouro atual: {jogador.gold} 🪙")
    escolha = input("Escolha o número do item que quer comprar (ou ENTER para cancelar): ").strip()
    if escolha == "":
        print("Compra cancelada.")
    else:
        try:
            indice = int(escolha) - 1
            if indice < 0 or indice >= len(lista_itens):
                raise Exception
            item, preco = lista_itens[indice]
            if item in ["Arma de classe", "Bastão Mágico", "Arco de Caça", "Adaga Afiada", "Martelo Sagrado", "Armadura de classe"]:
                if item in jogador.equipamentos:
                    print(f"Já possui {item}! Não pode comprar mais de um.")
                    input("Prima Enter para continuar...")
                    return
            if item in ["Poção de Vida", "Ração"]:
                try:
                    quantidade = int(input(f"Quantas unidades de {item} quer comprar? "))
                except:
                    quantidade = 1
                custo_total = preco * quantidade
                if jogador.gold >= custo_total:
                    jogador.gold -= custo_total
                    for _ in range(quantidade):
                        jogador.inventario.append(item)
                    print(f"Comprou {quantidade} {item}(s) com sucesso!")
                else:
                    print("Ouro insuficiente!")
            else:
                if jogador.gold >= preco:
                    jogador.gold -= preco
                    jogador.equipamentos.append(item)
                    print(f"Comprou {item} com sucesso!")
                else:
                    print("Ouro insuficiente!")
        except:
            print("Opção inválida.")
    input("Prima Enter para continuar...")

def jogo_principal(jogador):
    while True:
        if jogador.nivel >= 100:
            print(f"\nParabéns, {jogador.nome}! Atingiu o nível máximo e terminou a sua jornada!")
            input("Prima Enter para voltar ao menu...")
            break
        print("\n=== MENU DO JOGO ===")
        print("1 - Aventuras")
        print("2 - Ver estado")
        print("3 - Usar item")
        print("4 - Loja")
        print("5 - Descansar")
        print("6 - Trabalhar")
        print("7 - Sair para o menu")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                sucesso = menu_aventura(jogador)
                if sucesso is False:
                    break
            case "2":
                jogador.exibir_status()
            case "3":
                usar_item(jogador)
            case "4":
                loja(jogador)
            case "5":
                descansar(jogador)
            case "6":
                trabalhar(jogador)
            case "7":
                break
            case _:
                print("Opção inválida.")
                input("Prima Enter para continuar...")

while True:
    escolha = menu_inicial()
    if escolha == "1":
        limpar_ecrã()
        print("Vamos criar o seu personagem!")
        nome = input("Nome do jogador: ")
        idade = input("Idade: ")
        genero = input("Género (Masculino/Feminino/Outro): ")
        classe = escolher_classe()
        raca = escolher_raca()
        jogador = Jogador(nome, idade, genero, classe, raca)
        print(f"\nPersonagem criado com sucesso, {nome} o(a) {raca} {classe}!")
        input("Prima Enter para começar a aventura...")
        limpar_ecrã()
        jogo_principal(jogador)
    elif escolha == "2":
        print("\nAté à próxima, aventureiro!")
        break
    else:
        print("Opção inválida.")
        input("Prima Enter para continuar...")