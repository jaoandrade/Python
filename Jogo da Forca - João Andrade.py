import random  #Jogo da Forca com animais - João Andrade
c=0
vidas=6
n = random.randint(1, 10)
lista=["macaco","tigre","elefante","girafa","cao","gato","zebra","panda","camelo","esquilo","ovelha"]
for i in range (10):
    c+=1
    if c == n:
        palavra = lista[i]
acertos = ["_"] * len(palavra) 
print("Jogo da Forca com nomes de animais, tente adivinhar.")
while vidas > 0:
    print(acertos)
    tent = input("Digite uma letra: ").lower()
    if tent in acertos:
     print("Você já acertou essa letra!")
     continue
    if tent in palavra:
        for i in range(len(palavra)):
         if palavra[i] == tent:
            acertos[i] = tent
            print("Letra correta!")
    else:
        vidas -= 1 
        print("Erraste! Tens", vidas, "vidas.")
    if "_" not in acertos:
            print("Parabéns! Adivinhaste a palavra é",palavra)
            exit()