# import random

# num = int(input("Digite um número de 10 a 15: "))

# while(num < 10 or num > 15):
#     print("Valor inválido, digite novamente!")
#     num = int(input("Digite um número de 10 a 15: "))

# sorteio = random.randint(10, 15)

# if(num==sorteio):
#     print(f"Parabéns, você acertou: {sorteio}")
# else:
#     print(f"Você errou, o número era: {sorteio}")

import random
sorteio = random.randint(1, 10)
num = ""
while(num != sorteio):
    num = int(input("Digite um número: "))

    if(num == sorteio):
        print("Parabéns, você acertou!")
    else:
        print("Você errou, tente novamente!")