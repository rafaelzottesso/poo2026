"""
Crie uma função chamada verifica_par que receba um número
inteiro como parâmetro. A função deve retornar True se o número
for par ou False se o número for ímpar.
Teste a função apresentando o resultado na tela.
"""
def verifica_par(x):
    if (x % 2 == 0):
        return True
    # Não precisa do else porque o código só executa aqui
    # se não acontecer o if
    return False


# Primeiro criamos a função e depois o "programa principal"

x = int(input("Digite um número: "))

if (verifica_par(x)):
    print(f"O {x} é par")
else:
    print(f"O {x} não é par")

"""
Você foi contratado para criar um simulador de sistema de
estoque para uma loja agrícola.
O programa principal deve exibir um menu utilizando um laço
while com as seguintes opções:
1 - Cadastrar Produto (solicita o nome do produto e o seu
    preço, e salva cada informação em listas distintas.
2 - Listar Produtos (percorre as listas e exibe o nome e o
    preço de todos os itens cadastrados).
3 - Aplicar Desconto (solicita uma porcentagem ao usuário e
    chama uma função que atualiza os preços).
4 - Sair do programa.

Para a opção 3, crie uma função que receba a lista de preços
e a porcentagem de desconto como parâmetros.
A função deve percorrer a lista com um laço for, efetuar 
o cálculo matemático de desconto, alterar cada preço na lista
e retornar a lista atualizada.

O sistema também deve utilizar estruturas if/elif/else para
processar corretamente a opção escolhida no menu e exibir
mensagens de erro para opções inválidas.
"""
# A função tem uma lista e um valor por parâmetro
def calcDesconto(precos, p):
    # Percorre a lista pelos índices e o len(precos) calcula o tamanho da lista
    for i in range(0, len(precos)):
        # Calcula só o desconto
        desconto = precos[i] * (p/100)
        # Calcula o valor final
        valor = precos[i] - desconto
        # Atualiza o valor na lista
        precos[i] = valor
    
    # retorna a lista inteira, por isso fica fora do "for"
    return precos

# Variável para controlar o índice usado ao cadastrar o produto
indiceProd = 0
# Lista para o nome do produto com tamanho 10
produtos = [""] * 10
# Lista dinâmica em Python, ela é aumentada dinamicamente, diferente
# da lista anterior de nomes que foi criada com 10 de tamanho
precos = []

# Cria a variável com valor zero para o while ser True na primeira vez
opc = 0
while(opc != 4):
    # Exibe o menu e pede opção para o usuário
    print("1 - Cadastrar Produto ") 
    print("2 - Listar Produtos")
    print("3 - Aplicar Desconto")
    print("4 - Sair do programa")
    opc = int(input ("Digite um número de 1 á 4: "))
    
    # Verifica a opção digitada
    if(opc == 1):
        print("Cadastrar Produto ")
        nome = input("Nome: ")
        valor = float(input("valor: R$"))
        # Guarda o produto conforme a variável de controle do índice
        produtos[indiceProd] = nome
        # Aumenta o valor dela porque aquele índice anterior já foi usado
        # Se não aumentar, o Python sempre vai guardar no índice 0
        indiceProd +=1
        # Em listas dinâmicas usamos o "append" para adicionar um valor no final dela
        precos.append(valor)

    elif(opc == 2): 
        print("Listar Produtos")
        # Cria o for com os índices em "i" e como precos tem tamanho dinâmico
        # o len fica nele, pois a lista de nome de produtos tem tamanho 10
        # e no início do programa o preço não vai ter 10 de tamanho
        for i in range(0, len(precos)):
            # Acessa o mesmo índice nas duas listas, pois eles são preenchidos juntos
            # com os dados do mesmo produto. Sempre nos mesmos índices
            print(produtos[i], "-", precos[i])

    elif(opc == 3):
        print("Aplicar Desconto")
        desconto = int(input('Digite a porcentagem de desconto: '))
        # Passa para a função a lista de preços e a porcentagem de desconto
        preco_final = calcDesconto(precos, desconto)
        # Faz o for com os índices da lista de preços, mas todos tem o mesmo tamanho
        # porque são preenchidos juntos
        # o "preco_final" é uma cópia da lista original de preços, mas com o desconto aplicado
        for i in range(0, len(precos)):
            print(produtos[i], "-", preco_final[i])

    elif(opc == 4):
        print("Sair do programa")
        
    else:
        print("Opção inválida")   