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
# CLASSE BLOCO (PLATAFORMAS / CHÃO)
# ==========================================
class Bloco(arcade.Sprite):
    """
    Classe que representa um bloco sólido (chão ou plataforma suspensa).
    Herda da classe arcade.Sprite.
    """
    def __init__(self, x: float, y: float):
        # Chama o construtor da classe pai (arcade.Sprite) carregando a imagem do bloco com escala 1.0
        super().__init__("bloco.png", scale=1)
        # Define a posição inicial (coordenadas X e Y centrais) do bloco no momento da instanciação
        self.center_x = x
        self.center_y = y


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
    Herda da classe arcade.Sprite e gerencia a alternância de texturas ao mudar de direção.
    """
    # O método __init__ é o construtor da classe, onde definimos as características iniciais do objeto
    def __init__(self):
        # 1. Carrega as folhas de sprites (spritesheets) para a direita e esquerda
        sheet_direita = arcade.load_spritesheet("player_direita.png")

        # 2. Extrai a grade de texturas (cada quadro individual tem 252x247 px: 1008 / 4 = 252)
        quadros_direita = sheet_direita.get_texture_grid(
            size=(252, 247),  # Tamanho de CADA quadro (largura_individual, altura_individual)
            columns=4,
            count=4
        )
        
        # Criar quadros_esquerda para armazenar a imagem do player indo para esquerda
        quadros_esquerda = []
        # Para cada frame da imagem do player indo para direita
        for frame in quadros_direita:
            # Inverte horizontalmente e armazena em quadros_esquerda
            quadros_esquerda.append(frame.flip_left_right())

        # 3. Inicializa o Sprite com a primeira textura da lista (quadro 0)
        super().__init__(quadros_direita[0], scale=0.5)

        # 4. Mapeamento das Poses usando os índices da lista
        # [0] = Parado | [1] = Passo 1 | [2] = Passo 2 | [3] = Pulo
        self.textura_parado_d = quadros_direita[0]
        self.textura_parado_e = quadros_esquerda[0]

        self.passos_direita = [quadros_direita[1], quadros_direita[2]]
        self.passos_esquerda = [quadros_esquerda[1], quadros_esquerda[2]]

        self.textura_pulo_d = quadros_direita[3]
        self.textura_pulo_e = quadros_esquerda[3]

        # 5. Controladores de Estado e Animação
        self.quadro_atual: int = 0
        self.tempo_animacao: float = 0.0
        self.virado_para: str = "DIREITA"

    def update(self, delta_time: float = 1/60):
        # 1. Atualiza a direção que o personagem está olhando
        if self.change_x > 0:
            self.virado_para = "DIREITA"
        elif self.change_x < 0:
            self.virado_para = "ESQUERDA"

        # 2. ESTADO: NO AR / PULANDO (Prioridade Máxima)
        if self.change_y != 0:
            self.texture = self.textura_pulo_d if self.virado_para == "DIREITA" else self.textura_pulo_e
            return

        # 3. ESTADO: PARADO NO CHÃO
        if self.change_x == 0:
            self.texture = self.textura_parado_d if self.virado_para == "DIREITA" else self.textura_parado_e
            return

        # 4. ESTADO: ANDANDO NO CHÃO (Ciclo de Passos)
        self.tempo_animacao += delta_time
        if self.tempo_animacao >= 0.1:  # Troca de imagem a cada 100ms
            self.tempo_animacao = 0.0
            self.quadro_atual = (self.quadro_atual + 1) % len(self.passos_direita)

            if self.virado_para == "DIREITA":
                self.texture = self.passos_direita[self.quadro_atual]
            else:
                self.texture = self.passos_esquerda[self.quadro_atual]

        # Manter o Player dentro dos limites laterais da janela
        if self.right > LARGURA:
            self.right = LARGURA
        if self.left < 0:
            self.left = 0



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
        # Define a cor de fundo da janela ao exibir esta view
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
            tela_jogo = TelaJogo()            # Instancia a tela da partida
            self.window.show_view(tela_jogo)  # Troca a view ativa para a tela do jogo
        # Se pressionar 'ESC', encerra a aplicação
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


# ==========================================
# CLASSE TELA JOGO (PARTIDA)
# ==========================================
class TelaJogo(arcade.View):
    """
    Classe que gerencia toda a lógica, renderização e física da partida.
    Herda de arcade.View.
    """
    def __init__(self):
        # Chamar o construtor da classe pai (arcade.View)
        super().__init__()
        
        # Carregar a imagem de fundo do cenário do jogo
        self.fundo = arcade.load_texture("cenario.png")
        
        # Define a velocidade de movimento horizontal do jogador
        self.velocidade = 3
        # Armazena a pontuação acumulada pelo jogador
        self.pontuacao = 0
        
        # Armazena o tempo decorrido do jogo em segundos
        self.tempo_decorrido = 0.0
        # Armazena o timestamp do início da partida
        self.tempo_inicio = time.time()

        # Cria as listas de sprites que agrupam os elementos na tela
        self.sprite_moedas = arcade.SpriteList()   # Lista para armazenar todas as moedas
        self.sprite_jogador = arcade.SpriteList()  # Lista para armazenar o jogador
        self.sprite_blocos = arcade.SpriteList()   # Lista para armazenar os blocos do chão e plataformas

        # Instancia o objeto do personagem/jogador
        self.personagem = Player()
        # Posiciona o jogador no canto inferior esquerdo inicialmente
        self.personagem.left = 0
        self.personagem.bottom = 50
        # Adiciona o personagem na lista de sprites do jogador
        self.sprite_jogador.append(self.personagem)

        # Cria uma moeda inicial móvel
        self.moeda = Moeda()
        self.moeda.center_x = 100
        self.moeda.center_y = 150
        # Define velocidade para que esta moeda fique se movendo e rebatendo
        self.moeda.change_x = self.velocidade
        self.moeda.change_y = self.velocidade
        # Adiciona a moeda na lista de moedas
        self.sprite_moedas.append(self.moeda)

        # Laço de repetição para gerar 25 moedas adicionais em posições aleatórias
        for x in range(25):
            moeda_simples = Moeda()
            # Posiciona a moeda em coordenadas X e Y aleatórias dentro dos limites da tela
            moeda_simples.center_x = random.randint(50, LARGURA - 50)
            moeda_simples.center_y = random.randint(80, ALTURA - 50)
            # Adiciona a moeda gerada na lista de moedas
            self.sprite_moedas.append(moeda_simples)

        # Criação do chão sólido: blocos lado a lado na base da tela (largura de 64px cada)
        for x in range(32, LARGURA + 32, 64):
            chao = Bloco(x=x, y=10)
            self.sprite_blocos.append(chao)

        # Criação de plataformas suspensas com blocos em coordenadas predefinidas
        posicoes_plataforma = [(300, 250), (550, 250)]
        for x, y in posicoes_plataforma:
            plataforma = Bloco(x, y)
            self.sprite_blocos.append(plataforma)

        # Cria a engine de física com gravidade e detecção de colisão com os blocos
        self.engine_fisica = arcade.PhysicsEnginePlatformer(
            player_sprite=self.personagem,
            walls=self.sprite_blocos,
            gravity_constant=0.5
        )

    def on_show_view(self):
        # Define a cor de fundo da janela ao exibir a tela do jogo
        arcade.set_background_color(arcade.color.AMAZON)

    # Desenha todos os elementos visuais na tela a cada quadro
    def on_draw(self):
        # Limpa a tela
        self.clear()

        # Desenha o cenário de fundo centralizado e preenchendo toda a tela
        arcade.draw_texture_rect(
            texture=self.fundo,
            rect=arcade.XYWH(
                x=LARGURA / 2,
                y=ALTURA / 2,
                width=LARGURA,
                height=ALTURA
            )
        )

        # Desenha na tela todas as listas de sprites
        self.sprite_blocos.draw()   # Desenha os blocos do chão e plataformas
        self.sprite_moedas.draw()   # Desenha todas as moedas
        self.sprite_jogador.draw()  # Desenha o jogador

        # Desenha os textos informativos (HUD): pontuação e tempo decorrido
        arcade.draw_text(f"Moedas Coletadas: {self.pontuacao}", 10, 570, arcade.color.WHITE, 14, bold=True)
        arcade.draw_text(f"Tempo: {self.tempo_decorrido:.1f}s", 10, 545, arcade.color.WHITE, 14)

    # Atualiza a lógica do jogo (física, posições, colisões e condições de vitória)
    def on_update(self, delta_time):
        # Incrementa o tempo decorrido da partida
        self.tempo_decorrido += delta_time

        # Atualiza o motor de física (movimentação com gravidade e colisão com blocos)
        self.engine_fisica.update()

        # Atualiza o sprite do jogador (ajusta a textura conforme o estado/animação e checa limites)
        self.personagem.update(delta_time)

        # Atualiza a movimentação das moedas móveis
        self.sprite_moedas.update(delta_time)

        # Verifica se houve colisão entre o jogador e qualquer uma das moedas na lista
        moedas_colididas = arcade.check_for_collision_with_list(self.personagem, self.sprite_moedas)
        
        # Itera sobre cada moeda que colidiu com o jogador
        for moeda in moedas_colididas:
            # Remove a moeda da lista para que ela desapareça da tela
            moeda.remove_from_sprite_lists()
            
            # Se a moeda estava em movimento (change_x != 0 ou change_y != 0), concede 3 pontos; caso contrário, 1 ponto
            if moeda.change_x != 0 or moeda.change_y != 0:
                self.pontuacao += 3
            else:
                self.pontuacao += 1

        # Verifica se todas as moedas foram coletadas (condição de vitória)
        if len(self.sprite_moedas) == 0:
            # Calcula o tempo total real gasto na partida
            tempo_total = time.time() - self.tempo_inicio
            # Cria a tela de Game Over passando a pontuação final e o tempo total
            tela_game_over = TelaGameOver(pontuacao=self.pontuacao, tempo_jogo=tempo_total)
            # Transiciona a janela para a visualização de Game Over
            self.window.show_view(tela_game_over)

    # Trata os eventos de teclas pressionadas pelo jogador
    def on_key_press(self, key, modifiers):
        # Movimentação para a direita: velocidade positiva
        if key == arcade.key.RIGHT:
            self.personagem.change_x = self.velocidade
        # Movimentação para a esquerda: velocidade negativa
        elif key == arcade.key.LEFT:
            self.personagem.change_x = -self.velocidade

        # Mecânica de pulo: verifica se o jogador está sobre uma superfície sólida
        if key == arcade.key.UP or key == arcade.key.SPACE:
            if self.engine_fisica.can_jump():
                self.personagem.change_y = 16  # Aplica o impulso vertical para o pulo

        # Se pressionar ESC durante a partida, retorna ao menu inicial
        if key == arcade.key.ESCAPE:
            tela_inicial = TelaInicial()
            self.window.show_view(tela_inicial)

    # Trata os eventos ao soltar as teclas
    def on_key_release(self, key, modifiers):
        # Ao soltar a tecla de seta para a direita ou para a esquerda, para o movimento horizontal
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.personagem.change_x = 0


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
        # Define a cor de fundo para destacar as informações finais
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
    # Cria a janela principal do jogo com as dimensões e título definidos
    jogo = arcade.Window(LARGURA, ALTURA, TITULO)
    # Cria a instância da tela inicial (menu)
    tela_inicial = TelaInicial()
    # Define a tela inicial como a view ativa na janela
    jogo.show_view(tela_inicial)
    # Inicia o loop principal de eventos do Arcade
    arcade.run()


# Ponto de entrada do script Python
if __name__ == "__main__":
    executar()