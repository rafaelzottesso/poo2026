# from seu_arquivo import SuaClasse
from ex1_classes import Aluno, Turma 

pedro = Aluno("Pedro", 15, "Info")
joppew = Aluno("João Almeida", 67, "Info")
miguel = Aluno("Miguel Garcia Sorrilhia Neto", 15, "Info")

info2024 = Turma("INFO24", 2024)
info2024.estudantes.append(joppew)
info2024.estudantes.append(pedro)
info2024.estudantes.append(miguel)
info2024.exibir_estudantes()


# nome = input("Qual seu nome: ")
# idade = int(input("Qual sua idade: "))
# curso = input("Qual o curso que você está cursando: ")

# alun1 = Aluno(nome, idade, curso, [7, 10, 8])
# alun1.apresentar()
# ra = input("Qual seu RA: ")
# alun1.ra = ra
# alun1.apresentar()
# print(f"O nome é: {alun1.nome}")

# print(f"A média das notas é {alun1.calcular_media()}")
