meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho","julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
numero = int(input("Diga um número de 1 a 12: "))
if 1 <= numero <= 12:
    print("O mês correspondente é ",meses[numero - 1],".")
else:
    print("número inválido! 1-12.")  #Qual o mês? - João Andrade