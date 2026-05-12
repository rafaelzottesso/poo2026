# Importa as classes criadas no outro arquivo
from heranca_classes import Animal, Gato, Cachorro
# Cria um objeto Gato
# nome, especie e patas vão para o init de animal
# Jeane que é a dona vai para o init do Gato mesmo
mello = Gato("Mello","gato", 4, "Jeane") 
# Mostra só o nome do gato (exibe o valor atual do atributo)
print(f"meu gato é o {mello.nome}")
# Execuca os métodos do Gato
mello.respirar()
mello.ronronar()
mello.rugir()

# Cria um objeto do tipo Cachorro, que é também um Animal
# Esses dados vão para o init de animal e são definidos como atributos do objeto
floki = Cachorro("Floki", "cachoro", 4)
# Os métodos são executados todos que tem em Animal e em Cachorro
floki.abanar_rabo()
floki.respirar()
floki.rugir()