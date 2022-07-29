import random

# Começando co a definição do numero que pega número de 1 a 10 para você acertar
numero = random.randrange(1,10)
# Definindo a variavel adivinha com integração de input
adivinha =  int(input("Digite um número: "))

# while por que não quero colocar tentativas por enquanto, porém irei atualizar futuramente para 4 tentativas
while numero != adivinha:
    if adivinha < numero:
        print("Muito baixo mano")
        adivinha = int(input("Digite numero denovo ai: "))
    elif adivinha > numero:
        print("Muito alto!")
        adivinha = int(input("Digita denovo vai que acerta ne!: "))
    else:
        break
print("Ai sim agora acertou!! Parabéns")
