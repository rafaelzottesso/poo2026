import arcade # importar a biblioteca de jogos
import random # gerar números aleatórios

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
        if self.right > LARGURA or self.left < 0:
            self.change_x *= -1

        if self.top > ALTURA or self.bottom < 0:
            self.change_y *= -1


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

        # Manter o Player dentro da janela
        # Limita ele na borda da direita
        if self.right > LARGURA:
            self.change_x = 0
            self.right = LARGURA
        # Limita ele na borda da esquerda
        if self.left < 0:
            self.change_x = 0
            self.left = 0
        # Limita ele na borda de cima
        if self.top > ALTURA:
            self.change_y = 0
            self.top = ALTURA
        # Limita ele na borda inferior
        if self.bottom < 0:
            self.change_y = 0
            self.bottom = 0
        

# Criação da classe da janela do jogo, que herda da classe Window do Arcade
class JanelaJogo(arcade.Window):
    
    def __init__(self):
        
        # Chamar o construtor da classe pai (arcade.Window) para criar a janela do jogo com as dimensões e título definidos
        super().__init__(LARGURA, ALTURA, TITULO)
        # Definir a cor de fundo da janela
        arcade.set_background_color( arcade.color.AMAZON )
        
        # Define a velocidade do jogo
        self.velocidade = 3
        # Armazena a pontução do jogo
        self.pontuacao = 0

        # Cria as listas de sprites do jogo
        self.sprite_moedas = arcade.SpriteList()
        self.sprite_jogador = arcade.SpriteList()

        # Criar meu personagem
        self.personagem = Player()
        # Posicionar ele na tela
        self.personagem.left = 0
        self.personagem.bottom = 0
        # Adicionar o personagem na spriteList de jogador
        self.sprite_jogador.append(self.personagem)

        # Criar uma moeda
        self.moeda = Moeda()
        # Posicionar a moeda na tela
        self.moeda.center_x = 100
        self.moeda.center_y = 50
        # Adiciona movimento na moeda
        self.moeda.change_x = self.velocidade
        self.moeda.change_y = self.velocidade
        # Adicionar a moeda em um grupo de sprites
        self.sprite_moedas.append(self.moeda)

        # Cria um laço de repetição para criar 25 moedas
        for i in range(25):
            # Criar um objeto moeda
            self.moeda_simples = Moeda()
            # Posiciona no x aleatório
            self.moeda_simples.center_x = random.randint(50, LARGURA-50)
            self.moeda_simples.center_y = random.randint(50, ALTURA-50)
            
            # velocidade = random.randint(1,6)
            # if(velocidade < 3):
            #     if(velocidade %2 == 0):
            #         self.moeda_simples.change_x = velocidade
            #         self.moeda_simples.change_y = velocidade
            #     else:
            #         self.moeda_simples.change_x = -velocidade
            #         self.moeda_simples.change_y = -velocidade

            # Adicione a moeda na spritelist
            self.sprite_moedas.append(self.moeda_simples)


        # # Criar outra moeda
        # self.moeda2 = Moeda()
        # self.moeda2.left = 0
        # self.moeda2.bottom = 300

        # # Criar mais uma moeda
        # self.moeda3 = Moeda()
        # self.moeda3.left = 700
        # self.moeda3.bottom = 150

        # Adicionar a moeda em um grupo de sprites
        # self.sprite_moedas.append(self.moeda2)
        # self.sprite_moedas.append(self.moeda3)
    
    # Desenha coisas na tela
    def on_draw(self):
        self.clear()
        # Desenhar as listas de sprites
        self.sprite_jogador.draw()
        self.sprite_moedas.draw()

        # "Desenha" a pontuação na tela
        arcade.draw_text(f"Moedas Coletadas: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14)
    
    # Atualiza a lógica do jogo e das coisas que estão na tela
    def on_update(self, delta_time):
        # Atualizar as listas de sprites, o que chama o método update de cada sprite dentro da lista
        self.sprite_jogador.update(delta_time)
        self.sprite_moedas.update(delta_time)

        # Verifica se ouve colisão entre o player e a lista de moedas
        moedas_colididas = arcade.check_for_collision_with_list(self.personagem, self.sprite_moedas)
        # para cada moeda colidida
        for moeda in moedas_colididas:
            # Remove ela da lista de moedas
            moeda.remove_from_sprite_lists()
            # Se a moeda está em movimento, soma 3 pontos, se não soma 1
            # Precisa ser direfente de zero porque a velocidade dela pode ser + ou -
            if(moeda.change_x != 0):
                self.pontuacao += 3
            else:
                self.pontuacao += 1

    # Eventos de teclas pressionadas
    def on_key_press(self, key, modifiers):

        # Verifica a tecla pressionada e da o movimento no eixo certo
        if(key == arcade.key.RIGHT):
            self.personagem.change_x += self.velocidade
        elif(key == arcade.key.LEFT):
            self.personagem.change_x -= self.velocidade
        elif(key == arcade.key.UP):
            self.personagem.change_y += self.velocidade
        elif(key == arcade.key.DOWN):
            self.personagem.change_y -= self.velocidade

        # Se apertou ESC, sai do jogo
        if(key == arcade.key.ESCAPE):
            arcade.close_window()

    # Evento ao soltar as teclas
    def on_key_release(self, key, modifiers):
        if(key == arcade.key.RIGHT or key == arcade.key.LEFT):
            self.personagem.change_x = 0
        elif(key == arcade.key.UP or key == arcade.key.DOWN):
            self.personagem.change_y = 0

def executar():
    jogo = JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    executar()