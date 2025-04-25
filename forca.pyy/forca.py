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
limite_tentativas = len(palavra) + 8
acertou = False
enforcou = False

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

contador = 1
while(not acertou and not enforcou):
    
    resultado_formatado = "".join(letras_acertadas).capitalize()
    
    print(resultado_formatado)  
    print("Tentativas: ", contador, "/", limite_tentativas)
    chute = input("Digite a letra: ").lower() 
    print(chute)
    contador += 1

    indice = 0
    for letra in palavra:
        if chute == letra.lower():  
            letras_acertadas[indice] = letra  
        indice += 1

    if contador == limite_tentativas:
         enforcou = True

    if letras_acertadas.count("_") == 0:
        acertou = True
        print("Parabéns, você encontrou a palavra secreta")
        print(letras_acertadas) 


