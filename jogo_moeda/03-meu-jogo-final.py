import arcade  # Importar a biblioteca Arcade para desenvolvimento de jogos 2D
import random  # Importar módulo random para geração de números aleatórios
import time    # Importar módulo time para medição e manipulação de tempo

# ==========================================
# CONSTANTES DO JOGO
# ==========================================
# Cria constantes para centralizar dados que serão usados ao longo de todo o código
ALTURA = 600       # Altura da janela do jogo em pixels
LARGURA = 800      # Largura da janela do jogo em pixels
TITULO = "Meu jogo!"  # Título exibido na barra superior da janela


# ==========================================
# CLASSE MOEDA (ITENS COLETÁVEIS)
# ==========================================
class Moeda(arcade.Sprite):
    """
    Classe que representa a moeda coletável pelo jogador.
    Herda da classe arcade.Sprite.
    """
    # O método __init__ é o construtor da classe, onde definimos as características iniciais do objeto
    def __init__(self):
        # Carrega a imagem da moeda com escala reduzida para 0.6
        super().__init__("moeda.png", scale=0.6)
    
    # O método update é chamado a cada frame do jogo para atualizar a movimentação da moeda
    def update(self, delta_time: float = 1/60):
        # Atualiza a posição no eixo X e Y somando a velocidade atual
        self.center_x += self.change_x
        self.center_y += self.change_y

        # As bordas do elemento são usadas para verificar se ele saiu da tela,
        # e caso tenha atingido os limites horizontais, inverte a direção horizontal (change_x)
        if self.right > LARGURA or self.left < 0:
            self.change_x *= -1

        # Caso tenha atingido os limites verticais, inverte a direção vertical (change_y)
        if self.top > ALTURA or self.bottom < 0:
            self.change_y *= -1


# ==========================================
# CLASSE PLAYER (JOGADOR)
# ==========================================
class Player(arcade.Sprite):
    """
    Classe que representa o personagem controlado pelo jogador.
    Herda da classe arcade.Sprite e gerencia a movimentação e alternância de texturas.
    """
    # O método __init__ é o construtor da classe, onde definimos as características iniciais do objeto
    def __init__(self):
        # Inicializa o sprite com a imagem virada para a direita e escala 0.5
        super().__init__("direita.png", scale=0.5)
        # Carrega as texturas para quando o personagem estiver olhando para a direita e para a esquerda
        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")
    
    # O método update é chamado a cada frame do jogo para mover e atualizar a textura do personagem
    def update(self, delta_time: float = 1/60):
        # Adicionar a movimentação no eixo x e y
        self.center_x += self.change_x
        self.center_y += self.change_y
        
        # Verificar a direção do movimento horizontal para mudar a textura do personagem
        # Se estiver se movendo para a direita, usa a textura virada para a direita
        if self.change_x > 0:
            self.texture = self.textura_direita
        # Se estiver se movendo para a esquerda, usa a textura virada para a esquerda
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        # Manter o Player dentro dos limites da janela
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


# ==========================================
# CLASSE TELA INICIAL (MENU PRINCIPAL)
# ==========================================
class TelaInicial(arcade.View):
    """
    Classe que representa o menu inicial do jogo.
    Herda de arcade.View para permitir transições entre telas.
    """
    def __init__(self):
        # Chama o construtor da classe pai arcade.View
        super().__init__()
        
    def on_show_view(self):
        # Definir a cor de fundo da janela ao exibir esta tela
        arcade.set_background_color(arcade.color.AMAZON)
        
    def on_draw(self):
        # Limpa os desenhos da tela antes de desenhar o novo frame
        self.clear()
        # Desenha os textos informativos do menu centralizados na tela
        arcade.draw_text("COLETOR DE MOEDAS", LARGURA / 2, 400, arcade.color.WHITE, 32, anchor_x="center", bold=True)
        arcade.draw_text("Pressione [J] ou [ENTER] para Jogar", LARGURA / 2, 300, arcade.color.WHITE, 18, anchor_x="center")
        arcade.draw_text("Pressione [ESC] para Sair", LARGURA / 2, 240, arcade.color.WHITE, 18, anchor_x="center")

    def on_key_press(self, key, modifiers):
        # Se o usuário pressionar 'J' ou 'ENTER', instancia a tela do jogo e a exibe na janela
        if key == arcade.key.J or key == arcade.key.ENTER:
            tela_jogo = TelaJogo()            # Instancia a tela do jogo
            self.window.show_view(tela_jogo)  # Encaixa ela na janela ativa
        # Se pressionar 'ESC', encerra a aplicação
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


# ==========================================
# CLASSE TELA JOGO (PARTIDA)
# ==========================================
class TelaJogo(arcade.View):
    """
    Classe que gerencia toda a lógica e renderização da partida.
    Herda de arcade.View.
    """
    def __init__(self):
        # Chamar o construtor da classe pai (arcade.View)
        super().__init__()
        
        # Carregar a imagem de fundo do cenário do jogo
        self.fundo = arcade.load_texture("cenario.png")
        
        # Define a velocidade base de deslocamento do jogador
        self.velocidade = 3
        # Armazena a pontuação acumulada pelo jogador
        self.pontuacao = 0
        
        # Armazena o tempo decorrido do jogo em segundos
        self.tempo_decorrido = 0.0
        # Armazena o timestamp de início da partida para cálculo do tempo total
        self.tempo_inicio = time.time()

        # Cria as listas de sprites que agrupam os elementos na tela
        self.sprite_moedas = arcade.SpriteList()   # Lista para armazenar todas as moedas
        self.sprite_jogador = arcade.SpriteList()  # Lista para armazenar o jogador

        # Criar o personagem do jogador
        self.personagem = Player()
        # Posicionar o jogador no canto inferior esquerdo
        self.personagem.left = 0
        self.personagem.bottom = 0
        # Adicionar o personagem na spriteList de jogador
        self.sprite_jogador.append(self.personagem)

        # Criar uma moeda inicial em movimento
        self.moeda = Moeda()
        # Posicionar a moeda na tela
        self.moeda.center_x = 100
        self.moeda.center_y = 50
        # Adiciona movimento na moeda
        self.moeda.change_x = self.velocidade
        self.moeda.change_y = self.velocidade
        # Adicionar a moeda ao grupo de sprites de moedas
        self.sprite_moedas.append(self.moeda)

        # Cria um laço de repetição para criar 25 moedas adicionais
        for _ in range(25):
            # Criar um objeto moeda
            moeda_simples = Moeda()
            # Posiciona em coordenadas X e Y aleatórias dentro dos limites
            moeda_simples.center_x = random.randint(50, LARGURA - 50)
            moeda_simples.center_y = random.randint(50, ALTURA - 50)
            # Adiciona a moeda gerada na lista de moedas
            self.sprite_moedas.append(moeda_simples)

    def on_show_view(self):
        # Definir a cor de fundo da janela ao exibir a tela do jogo
        arcade.set_background_color(arcade.color.AMAZON)
    
    # Desenha todos os elementos visuais na tela a cada quadro
    def on_draw(self):
        # Limpa a tela
        self.clear()

        # Desenha o cenário centralizado e esticado para o tamanho total da tela
        arcade.draw_texture_rect(
            texture=self.fundo,
            rect=arcade.XYWH(
                x=LARGURA / 2,
                y=ALTURA / 2,
                width=LARGURA,
                height=ALTURA
            )
        )

        # Desenhar as listas de sprites na tela
        self.sprite_jogador.draw()
        self.sprite_moedas.draw()

        # Desenha os textos informativos (HUD): pontuação e tempo decorrido
        arcade.draw_text(f"Moedas Coletadas: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14, bold=True)
        arcade.draw_text(f"Tempo: {self.tempo_decorrido:.1f}s", 10, 545, arcade.color.WHITE, 14)
    
    # Atualiza a lógica do jogo e das coisas que estão na tela
    def on_update(self, delta_time):
        # Incrementa o tempo decorrido da partida
        self.tempo_decorrido += delta_time

        # Atualizar as listas de sprites, chamando o método update de cada sprite
        self.sprite_jogador.update(delta_time)
        self.sprite_moedas.update(delta_time)

        # Verifica se houve colisão entre o jogador e a lista de moedas
        moedas_colididas = arcade.check_for_collision_with_list(self.personagem, self.sprite_moedas)
        
        # Para cada moeda colidida
        for moeda in moedas_colididas:
            # Remove a moeda da lista para que suma da tela
            moeda.remove_from_sprite_lists()
            
            # Se a moeda está em movimento (change_x != 0 ou change_y != 0), soma 3 pontos; se parada, soma 1
            if moeda.change_x != 0 or moeda.change_y != 0:
                self.pontuacao += 3
            else:
                self.pontuacao += 1

        # Verificar se todas as moedas foram coletadas (condição de vitória)
        if len(self.sprite_moedas) == 0:
            # Calcula o tempo total gasto na partida
            tempo_total = time.time() - self.tempo_inicio
            # Cria a tela de Game Over passando a pontuação final e o tempo total
            tela_game_over = TelaGameOver(pontuacao=self.pontuacao, tempo_jogo=tempo_total)
            # Transiciona para a tela de Game Over
            self.window.show_view(tela_game_over)

    # Eventos de teclas pressionadas
    def on_key_press(self, key, modifiers):
        # Verifica a tecla pressionada e aplica a velocidade e textura na direção correspondente
        if key == arcade.key.RIGHT:
            self.personagem.change_x = self.velocidade
            self.personagem.texture = self.personagem.textura_direita
        elif key == arcade.key.LEFT:
            self.personagem.change_x = -self.velocidade
            self.personagem.texture = self.personagem.textura_esquerda
        elif key == arcade.key.UP:
            self.personagem.change_y = self.velocidade
        elif key == arcade.key.DOWN:
            self.personagem.change_y = -self.velocidade

        # Se apertou ESC, volta para a tela inicial
        if key == arcade.key.ESCAPE:
            tela_inicial = TelaInicial()
            self.window.show_view(tela_inicial)

    # Evento ao soltar as teclas
    def on_key_release(self, key, modifiers):
        # Ao soltar as teclas de movimento horizontal, zera o change_x
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.personagem.change_x = 0
        # Ao soltar as teclas de movimento vertical, zera o change_y
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.personagem.change_y = 0


# ==========================================
# CLASSE TELA GAME OVER (FIM DE JOGO / VITÓRIA)
# ==========================================
class TelaGameOver(arcade.View):
    """
    Classe que representa a tela de Game Over / Vitória ao finalizar o jogo.
    Exibe a pontuação total e o tempo total de jogo decorrido.
    """
    def __init__(self, pontuacao: int, tempo_jogo: float):
        # Chama o construtor da classe pai arcade.View
        super().__init__()
        # Armazena os resultados da partida recebidos como parâmetro
        self.pontuacao = pontuacao
        self.tempo_jogo = tempo_jogo

    def on_show_view(self):
        # Define a cor de fundo para a tela final
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        # Limpa o conteúdo da tela antes de desenhar
        self.clear()

        # Desenha o título de vitória centralizado no topo
        arcade.draw_text(
            "PARABÉNS! VOCÊ VENCEU!",
            LARGURA / 2,
            430,
            arcade.color.WHITE,
            28,
            anchor_x="center",
            bold=True
        )

        # Formata o tempo de jogo em minutos e segundos caso ultrapasse 60s, ou apenas segundos
        minutos = int(self.tempo_jogo // 60)
        segundos = self.tempo_jogo % 60
        if minutos > 0:
            texto_tempo = f"Tempo de Jogo: {minutos}m {segundos:.1f}s"
        else:
            texto_tempo = f"Tempo de Jogo: {segundos:.1f}s"

        # Desenha a pontuação final obtida pelo jogador
        arcade.draw_text(
            f"Pontuação Final: {self.pontuacao} pontos",
            LARGURA / 2,
            330,
            arcade.color.WHITE,
            22,
            anchor_x="center"
        )

        # Desenha o tempo total de jogo
        arcade.draw_text(
            texto_tempo,
            LARGURA / 2,
            275,
            arcade.color.WHITE,
            22,
            anchor_x="center"
        )

        # Desenha as opções de navegação pós-jogo
        arcade.draw_text(
            "Pressione [J] ou [ENTER] para Jogar Novamente",
            LARGURA / 2,
            180,
            arcade.color.WHITE,
            16,
            anchor_x="center"
        )
        arcade.draw_text(
            "Pressione [ESC] para Voltar ao Menu Inicial",
            LARGURA / 2,
            135,
            arcade.color.WHITE,
            16,
            anchor_x="center"
        )

    def on_key_press(self, key, modifiers):
        # Se pressionar J ou ENTER, reinicia uma nova partida
        if key == arcade.key.J or key == arcade.key.ENTER:
            tela_jogo = TelaJogo()
            self.window.show_view(tela_jogo)
        # Se pressionar ESC, retorna para a tela inicial / menu
        elif key == arcade.key.ESCAPE:
            tela_inicial = TelaInicial()
            self.window.show_view(tela_inicial)


# ==========================================
# FUNÇÃO PRINCIPAL DE EXECUÇÃO
# ==========================================
def executar():
    # Cria a janela principal do jogo com os parâmetros
    jogo = arcade.Window(LARGURA, ALTURA, TITULO)
    # Cria uma tela inicial
    tela_inicial = TelaInicial()
    # Coloca essa tela inicial na janela do jogo
    jogo.show_view(tela_inicial)
    # Executa o arcade
    arcade.run()


# Ponto de entrada do script Python
if __name__ == "__main__":
    executar()