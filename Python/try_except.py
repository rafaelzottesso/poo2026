# Tratamento de exceções em Python
# O comando "try" tenta executar um código qualquer em Python
try:
    idade = int(input("idade: "))
    idade_nova = idade + 5
    print("Sua idade daqui 5 anos será", idade_nova)
# Se der algum erro na execução do código, o Python não vai finalizar o programa
# Em vez disso, vai executar o código abaixo
except Exception as erro:
    # Você pode criar variáveis, fazer if/else/, repetição, qualquer coisa aqui
    print("Idade inválida!!")
    # A mensagem de erro pode ser capturada transformando em str o erro
    print(str(erro))

# O try/except deve ser usado em instruções limitadas e não no programa inteiro