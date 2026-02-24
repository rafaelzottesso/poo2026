print("Programação Orientada a Objetos")

nome = input("Nome: ")
idade = input("Idade: ")
idade = int(idade)
salario = float(input("Salário: R$"))

# print("Olá", nome, ". Você tem", idade, "anos.")
# str formatada
print(f"Olá {nome}. Você tem {idade} anos.")

if(salario <= 10000):
    print(f"Você ganha muito mal: R${salario:.2f}")
else:
    print(f"Você ganha bem!! R${salario:.2f}")