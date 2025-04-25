import random
palavras = []

print("1-animais\n2-comidas\n3-series")
opcao =int(input("digite o tema desejado:"))
if opcao== 1:
    arquivo=open("animais.txt","r")
elif opcao ==2:
    arquivo=open("comidas.txt","r")
elif opcao==3:
    arquivo=open("series.txt","r")
else:
    print("opção inexistente, selecionada opção1")
    arquivo = open("animais.txt","r")

for linha in arquivo:
    palavras.append(linha.strip())

#print(palavras)


palavra = random.choice(palavras)
limite_tentativas = len(palavra) + 5
acertou = False  
enforcou = False  
letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")  


contador = 1


while not acertou and not enforcou:
    resultado_formatado = "".join(letras_acertadas).capitalize()
    print(f"\nPalavra: {resultado_formatado}")
    print(f"Tentativas: {contador}/{limite_tentativas}")
    
    chute = input("Digite uma letra: ").lower()

    if chute in palavra.lower():
        for indice, letra in enumerate(palavra):
            if chute == letra.lower():
                letras_acertadas[indice] = letra
    else:
        print(f"Letra '{chute}' não está na palavra!")
        contador += 1

    # Condições para o fim do jogo
    if contador >= limite_tentativas:
        enforcou = True
        print("\nVocê perdeu! A palavra era:", palavra)
    elif "_" not in letras_acertadas:
        acertou = True
        print("\nParabéns, você encontrou a palavra secreta!")
        print("Palavra:", "".join(letras_acertadas))


