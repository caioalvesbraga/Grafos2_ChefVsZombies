import pygame
import random
import math
import itertools

pygame.init()
pygame.mixer.quit()

LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Aventura do Chef Desastrado")

chef_img = pygame.image.load('assets/chef.png')
zombie_img = pygame.image.load('assets/zombie.png')
food_img = pygame.image.load('assets/food.png')

chef_img = pygame.transform.scale(chef_img, (50, 50))  
zombie_img = pygame.transform.scale(zombie_img, (50, 50))
food_img = pygame.transform.scale(food_img, (30, 30))

clock = pygame.time.Clock()

def desenhar_jogador(x, y):
    tela.blit(chef_img, (x, y))

def desenhar_ingredientes(ingredientes):
    for ingrediente in ingredientes:
        tela.blit(food_img, ingrediente)

def desenhar_inimigos(inimigos):
    for inimigo in inimigos:
        tela.blit(zombie_img, inimigo)

def mover_jogador(x, y, teclas):
    if teclas[pygame.K_LEFT] and x > 0:
        x -= 5
    if teclas[pygame.K_RIGHT] and x < LARGURA_TELA - 50:
        x += 5
    if teclas[pygame.K_UP] and y > 0:
        y -= 5
    if teclas[pygame.K_DOWN] and y < ALTURA_TELA - 50:
        y += 5
    return x, y

def calcular_distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calcular_caminho_total(caminho, chef_inicio):
    custo_total = 0
    ponto_atual = chef_inicio
    
    for ponto in caminho:
        custo_total += calcular_distancia(ponto_atual, ponto)
        ponto_atual = ponto
    
    return custo_total

# Função para resolver o problema do caixeiro-viajante
def tsp(chef_inicio, ingredientes):
    permutacoes = itertools.permutations(ingredientes)
    menor_custo = float('inf')
    melhor_caminho = None
    
    for caminho in permutacoes:
        custo = calcular_caminho_total(caminho, chef_inicio)
        if custo < menor_custo:
            menor_custo = custo
            melhor_caminho = caminho
    
    return melhor_caminho

def gerar_ingredientes():
    ingredientes = []
    for _ in range(3):
        x = random.randint(50, LARGURA_TELA - 50)
        y = random.randint(50, ALTURA_TELA - 50)
        ingredientes.append((x, y))
    return ingredientes

# Função para verificar se o jogador encontrou todos os ingredientes
def verificar_vitoria(jogador_x, jogador_y, ingredientes):
    for ingrediente in ingredientes:
        if abs(jogador_x - ingrediente[0]) < 30 and abs(jogador_y - ingrediente[1]) < 30:
            ingredientes.remove(ingrediente)
    return len(ingredientes) == 0

# Função para desenhar o caminho calculado pelo algoritmo de Dijkstra (TSP)
def desenhar_caminho(caminho, caminho_visitado):
    # Desenhar apenas as linhas conectando os pontos do caminho
    for i in range(len(caminho) - 1):
        if caminho[i] not in caminho_visitado and caminho[i+1] not in caminho_visitado:
            pygame.draw.line(tela, (0, 255, 255), caminho[i], caminho[i+1], 2)

# Função para mover os zumbis em direção ao chef
def mover_zumbis(inimigos, jogador_x, jogador_y):
    for i in range(len(inimigos)):
        zumbi_x, zumbi_y = inimigos[i]
        
        # Movimento simples do zumbi em direção ao chef
        if zumbi_x < jogador_x:
            zumbi_x += 1
        elif zumbi_x > jogador_x:
            zumbi_x -= 1
        
        if zumbi_y < jogador_y:
            zumbi_y += 1
        elif zumbi_y > jogador_y:
            zumbi_y -= 1

        inimigos[i] = (zumbi_x, zumbi_y)

# Grafo (Agora, o grafo está fora da função jogo para ser acessado globalmente)
grafo = {}

# Função principal do jogo
def jogo():
    jogador_x = LARGURA_TELA // 2
    jogador_y = ALTURA_TELA // 2
    ingredientes = gerar_ingredientes()

    # Inimigos engraçados como "zumbis dançarinos"
    inimigos = [(random.randint(100, 700), random.randint(100, 500)) for _ in range(3)]

    # Posição inicial do chef
    chef_inicio = (jogador_x, jogador_y)

    # Resolver o TSP e obter o melhor caminho para pegar todos os ingredientes
    melhor_caminho = tsp(chef_inicio, ingredientes)

    # Lista para rastrear o caminho já percorrido
    caminho_visitado = []

    # Rodando o jogo
    jogo_rodando = True
    while jogo_rodando:
        tela.fill((0, 0, 0))  # Limpar a tela antes de desenhar (sem fundo)

        # Verificando eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

        # Movimentação do jogador
        teclas = pygame.key.get_pressed()
        jogador_x, jogador_y = mover_jogador(jogador_x, jogador_y, teclas)

        # Verificar se o jogador chegou a um ponto de ingrediente e atualizar o grafo
        for ingrediente in ingredientes[:]:
            if abs(jogador_x - ingrediente[0]) < 30 and abs(jogador_y - ingrediente[1]) < 30:
                ingredientes.remove(ingrediente)
                caminho_visitado.append(ingrediente)  # Marcar o ingrediente como visitado

        # Desenhar o jogador, os ingredientes e inimigos
        desenhar_jogador(jogador_x, jogador_y)
        desenhar_ingredientes(ingredientes)
        desenhar_inimigos(inimigos)

        # Desenhar o caminho calculado, apagando o que já foi percorrido
        desenhar_caminho(melhor_caminho, caminho_visitado)


        # Verificar se o jogador coletou todos os ingredientes
        if verificar_vitoria(jogador_x, jogador_y, ingredientes):
            print("Você coletou todos os ingredientes secretos! Vitória!")
            jogo_rodando = False

        pygame.display.update()
        clock.tick(60)  # 60 frames por segundo

    pygame.quit()

# Iniciar o jogo
jogo()