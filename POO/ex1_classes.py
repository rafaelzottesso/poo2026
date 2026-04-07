# Criação da classe aluno
class Aluno:

    # Método construtor do aluno
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
        # self.notas = notas

    # Método adicional
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        # while(self.ra == ""):
        #     print("Esse aluno não tem RA.")
        #     self.ra = input("Infome o RA: ")
       
        print(f"O RA é: {self.ra}")
    
    # Método adicional
    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.notas)):
            soma += self.notas[i]
        media = soma/len(self.notas)
        return media   
    
class Turma:

    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.estudantes = []

    def apresentar(self):
        print(f"{self.nome} - {self.ano}")

    def exibir_estudantes(self):
        for aluno in self.estudantes:
            aluno.apresentar()
