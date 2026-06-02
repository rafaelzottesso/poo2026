import arcade

# Cria constantes para centralizar dados que serão usados ao longo do código
ALTURA = 600
LARGURA = 800
TITULO = "Meu jogo!"

# Criação da classe da moeda, que herda da classe Sprite do Arcade
class Moeda(arcade.Sprite):
    # O método __init__ é o construtor da classe, onde definimos as características iniciais do objeto
    def __init__(self):
        super().__init__("moeda.png", scale=0.6)
    # O método update é chamado a cada frame do jogo, e é onde colocamos a lógica de movimentação ou outras ações que o objeto deve realizar
    def update(self, delta_time):
        # Adicionar a movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y

        # As bordas do elemento são usadas para verificar se ele saiu da tela, e caso tenha saído, a velocidade é zerada para que ele pare de se mover
        # Temos os lados right, left, top e bottom
        if self.right > LARGURA:
            self.change_x = 0
        
        elif self.left < 0:
            self.change_x = 0

        if self.top > ALTURA:
            self.change_y = 0

        elif self.bottom < 0:
            self.change_y = 0

# Criação da classe do jogador, que herda da classe Sprite do Arcade
class Player(arcade.Sprite):
    # O método __init__ é o construtor da classe, onde definimos as características iniciais do objeto
    def __init__(self):
        super().__init__("direita.png", scale=0.3)
        # Carregar as texturas para as direções do personagem
        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")
    # O método update é chamado a cada frame do jogo, e é onde colocamos a lógica de movimentação ou outras ações que o objeto deve realizar
    def update(self, delta_time):
        # Adicionar a movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y
        # Verificar a direção do movimento para mudar a textura do personagem
        # Se for zero, o personagem mantém a textura atual
        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

# Criação da classe da janela do jogo, que herda da classe Window do Arcade
class JanelaJogo(arcade.Window):
    def __init__(self):
        # Chamar o construtor da classe pai (arcade.Window) para criar a janela do jogo com as dimensões e título definidos
        super().__init__(LARGURA, ALTURA, TITULO)
        # Definir a cor de fundo da janela
        arcade.set_background_color( arcade.color.AMAZON )
        
        # Define a velocidade do jogo
        self.movimento = 3

        # Criar meu personagem
        self.personagem = Player()
        # Posicionar ele na tela
        self.personagem.center_x = 400
        self.personagem.center_y = 300

        # Adicionar o personagem em um grupo de sprites
        self.sprite_jogador = arcade.SpriteList()
        self.sprite_jogador.append(self.personagem)

        # Criar uma moeda
        self.moeda = Moeda()
        # Posicionar a moeda na tela
        self.moeda.center_x = 100
        self.moeda.center_y = 50
        # Adiciona movimento na moeda
        self.moeda.change_x = self.movimento
        self.moeda.change_y = self.movimento

        # Adicionar a moeda em um grupo de sprites
        self.sprite_moedas = arcade.SpriteList()
        self.sprite_moedas.append(self.moeda)
    
    # Desenha coisas na tela
    def on_draw(self):
        self.clear()
        # Desenhar as listas de sprites
        self.sprite_jogador.draw()
        self.sprite_moedas.draw()
    
    # Atualiza a lógica do jogo e das coisas que estão na tela
    def on_update(self, delta_time):
        # Atualizar as listas de sprites, o que chama o método update de cada sprite dentro da lista
        self.sprite_jogador.update(delta_time)
        self.sprite_moedas.update(delta_time)

def executar():
    jogo = JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    executar()