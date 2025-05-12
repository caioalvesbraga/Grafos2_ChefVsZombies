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