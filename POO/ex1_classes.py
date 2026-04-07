# Criação da classe aluno
class Aluno:

    # Método construtor do aluno com os atributos que são obrigatórios: nome, idade e curso
    def __init__(self, nome, idade, curso):
        # O self indica que os atributos vão ter valores diferentes para cada objeto
        # Porque um aluno será o Pedro, o João, a Maria, etc
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = "" # opcional
        self.notas = [] # opcional, mas será uma lista (vazia por enquanto)

    # Método para exibir os dados do aluno
    # Todo método precisa do self para poder acessar os atributos de cada objeto
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e faço o curso de {self.curso}.")
        # Verifica se já tem o RA do aluno e exibe uma mensagem na tela
        if(self.ra == ""):
            print("Esse aluno não tem RA.")
        else:
            print(f"O RA é: {self.ra}")
    
    # Percorre a lista de notas, independente do tamanho dela
    # Faz a soma das notas e depois a média conforme a quantidade de notas existentes (len())
    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.notas)):
            soma += self.notas[i] # acrescente o valor das notas à variável soma
        media = soma/len(self.notas) # faz a média
        return media # retorna a média e não exibe automaticamente na tela
    

# Cria uma classe para a turma    
class Turma:

    # A turma tem nome e ano obrigatórios
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.estudantes = [] # Será uma lista de estudantes preenchida com o .append(valor)

    # Exibe os dados da turma na tela
    def apresentar(self):
        print(f"{self.nome} - {self.ano}")

    # Método para percorrer a lista de estudantes e exibir seus dados na tela
    def exibir_estudantes(self):
        # Percorre a lista de estudantes pelos valores e NÃO pelo índice igual o for i in range faz
        # a variável aluno recebe o valor que está armazenado e não os índices 0, 1, 2, etc igual o "i"
        for aluno in self.estudantes:
            # como estudantes é uma lista com objetos, podemos acessar o método de um objeto
            # no caso de Aluno, tem o método apresentar() que exibe as informações do aluno na tela
            aluno.apresentar()
