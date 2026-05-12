class Animal:
    # Definir atributos e os obrigatórios
    def __init__(self, nome, especie, patas):
        self.nome = nome
        self.especie = especie
        self.patas = patas
        
    # Definir método e comportamento
    def respirar(self):
        print("Respirando...")

    # Definir método e comportamento
    def rugir(self):
        print("O animal vai rugir!")

# Criando uma herança para a classe Animal
# Agora Gato é um animal
class Gato(Animal):
    # O init deve pedir os atributos obrigatórios
    def __init__(self, nome, especie, patas, dono):
        # O super() chama um método da classe pai
        # E o init da classe pai precisa de nome, especie e patas
        super().__init__(nome, especie, patas)
        # Já a classe Gato tem o atributo "dono" que Animal não tem
        self.dono = dono
 
    # Esse seria o init sem usar o super, você precisa fazer tudo "na mão" novamente
    # def __init__(self, nome, especie, patas, dono):
    #     self.nome = nome
    #     self.especie = especie
    #     self.patas = patas
    #     self.dono = dono

    # Método da classe Gato
    def ronronar(self):
        print("ronronando...")

    # Fazendo a sobrescrita do método rugir
    # Agora o rugir de todos os Gatos vai funcionar assim e não como foi feito no Animal
    def rugir(self):
        print("Miau")

# CRia a classe Cachorro com Herança para ANimal
class Cachorro(Animal):
    # O init se não for sobrescrito vai usar o init da classe animal
    # Com os mesmos atributos que foram criados lá. Nenhum adicional vai ter para Cachorro
    def abanar_rabo(self):
        print("abanando...")

    # Sobrescreve o método, e agora todo cachorro vai rugir dessa forma e não como Animal
    def rugir(self):
        print("auu auu")