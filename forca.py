import random
from palavras import words

def linha():
    print()
    print("*" * 50)
    print()

palavra = random.choice(words).upper()
palavrasDigitadas = ''
erros = 0
maxErros = 10

forca = [" _ " for i in range(0, len(palavra))]

linha()
print(" Jogo da FORCA ".center(50))
linha()

while True:
    print(f"Palavras digitadas: {palavrasDigitadas}\n")
    print(f"Erros: {erros}\n")
    print("Forca: ", end='')
    for i in forca: print(i, end='')
    print("\n")

    if(not " _ " in forca): break
    
    escolha = '12'
    while len(escolha) > 1 or not escolha.isalpha():
        escolha = input("Digite uma letra: ").upper()

    if(escolha in palavra):
        cont = 0
        for i in palavra:
            if(i == escolha): forca[cont] = escolha
            cont += 1
    else:
        erros += 1
    
    if(erros == maxErros):
        print(f"Você perdeu. A palavra era: \'{palavra}\'")
        break

    palavrasDigitadas += escolha +" "
    linha()


linha()
print("Acabou ")