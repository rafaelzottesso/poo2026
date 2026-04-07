# from seu_arquivo import SuaClasse
# Importa as classes criadas em outro arquivo
from ex1_classes import Aluno, Turma 

# Cria "na mão" três objetos
# se não teria que fazer um monte de input
pedro = Aluno("Pedro", 15, "Info")
joppew = Aluno("João Almeida", 67, "Info")
miguel = Aluno("Miguel Garcia Sorrilhia Neto", 15, "Info")

# Cria uma turma
info2024 = Turma("INFO24", 2024)
# Usa o .append no atributo estudantes que é uma lista vazia []
info2024.estudantes.append(joppew) # adiciona um objeto nela
info2024.estudantes.append(pedro) # adiciona outro objeto nela
info2024.estudantes.append(miguel) # adiciona mais um objeto nela
# Executa o método que percorre a lista e exibe as informaçõies na tela
info2024.exibir_estudantes()

# Outra forma de criar objetos, mas usando o input para o usuário criar com seus dados desejados
# nome = input("Qual seu nome: ")
# idade = int(input("Qual sua idade: "))
# curso = input("Qual o curso que você está cursando: ")

# Cria o objeto com os dados fornecidos pelo usuário
# alun1 = Aluno(nome, idade, curso, [7, 10, 8])
# Executa o método
# alun1.apresentar()
# ra = input("Qual seu RA: ")
# alun1.ra = ra
# alun1.apresentar()
# print(f"O nome é: {alun1.nome}")

# print(f"A média das notas é {alun1.calcular_media()}")
