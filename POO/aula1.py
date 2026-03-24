# Criação da classe Campus
class Campus:
    # Método construtor é obrigatório
    # Todo método deve ter o parâmetro "self"
    def __init__(self):
        # self acessa os atributos do objeto
        self.nome = ""
        self.endereco = ""
    # Método usado ao "imprimir" um objeto
    def __str__(self):
        return f"Campus: {self.nome}"
    
# CRiação da classe Estudante
class Estudante:
    # O construtor tem o atributo nome como obrigatório
    def __init__(self, nome):
        self.nome = nome
        self.cpf = ""
        self.data_nasc = ""
    def __str__(self):
        return f"Estudante: {self.nome}"
    
    # Criar um método para a classe Estudante
    def apresentar(self):
        print(f"O(a) {self.nome} nasceu em {self.data_nasc}")
        if(self.cpf == ""):
            print("O(a) estudante não cadastrou CPF.")
        else:
            print("CPF:", self.cpf[0:3], "...")

# Criação dos objetos
# Criar um objeto para o estudante Ryan
# nome_do_objeto = Classe_Do_Objeto()
# nome_do_objeto.atributo1 = "Valor"
# nome_do_objeto.atributo2 = "Valor 2"
# nome_do_objeto.atributo3 = 158.99
# nome_do_objeto.método1()
# nome_do_objeto.método2()

# Cria o objeto e informa o valor do nome obrigatoriamente
ryan = Estudante("Ryan Carlos")
ryan.cpf = "123.456.789-00"
ryan.data_nasc = "22/01/2001"
ryan.apresentar()
