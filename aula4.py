alunos = [""] * 5
for i in range(0, len(alunos)):
    alunos[i] = input("Nome: ")

print("Lista de alunos:")
i = 0
while(i<5):
    print(f"Aluno {i+1}: {alunos[i]}")
