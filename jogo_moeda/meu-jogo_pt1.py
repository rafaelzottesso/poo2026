import arcade

# Cria constantes para centralizar dados que serão usados ao longo do código
ALTURA = 600
LARGURA = 800
TITULO = "Meu jogo!"

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__("direita.png", scale=0.3)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")

    def update(self, delta_time):
        pass


class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA, ALTURA, TITULO)
        arcade.set_background_color( arcade.color.AMAZON )

        # Criar meu personagem
        self.personagem = Player()
        # Posicionar ele na tela
        self.personagem.center_x = 400
        self.personagem.center_y = 300
    
    # Desenha coisas na tela
    def on_draw(self):
        self.clear()
        # Desenhar meu personagem
        arcade.draw_sprite( self.personagem )
    
    def on_update(self, delta_time):
        pass

def executar():
    jogo = JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    executar()