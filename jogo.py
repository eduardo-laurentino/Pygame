import pygame
import random
from pygame import mixer
import sys

# Inicializa o Pygame
# Aqui faço a inicialização da biblioteca Pygame
pygame.init()
mixer.init()
pygame.font.init()
fonte = pygame.font.SysFont('Comic Sans MS', 50) 

mixer.music.load('audio/corrida.wav')
mixer.music.set_volume(0.2)
mixer.music.play()

# Configurações da tela
LARGURA, ALTURA = 1000, 800
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Corrida")

# Carregar imagem da pista
pista = pygame.image.load("imagens/pista.png")  # Substitua por sua imagem
pista = pygame.transform.scale(pista, (LARGURA, ALTURA))  # Redimensiona para encaixar na tela

# Posição inicial da pista
pista_y1 = 0
pista_y2 = -ALTURA  # Segunda cópia da pista logo acima da primeira
velocidade_pista = 4  # Velocidade do movimento

# Configurações do carro
carro_largura = 80
carro_altura = 120
carro = pygame.image.load('imagens/carro.png')  
carro = pygame.transform.scale(carro, (carro_largura, carro_altura))
#carro = carro.get_rect(topLeft())
# Posição inicial do carro
x = (LARGURA * 0.45)
y = (ALTURA * 0.8)

# Configurações dos carros (Obstáculo)

obstaculo_largura = 50
obstaculo_altura = 100
obstaculo_velocidade = -0.1
lista_carros_obstaculos = ['carro_obstaculo_amarelo.png', 'carro_obstaculo_azul.png', 'carro_obstaculo_preto.png', 'carro_obstaculo_vermelho.png']

# Cria uma lista de dicionários com os carros obtáculos
obstaculos = []
for _ in range(len(lista_carros_obstaculos)):
    carro_selecionado = random.randrange(0, len(lista_carros_obstaculos)-1)
    carro_obstaculo = pygame.image.load('imagens/'+lista_carros_obstaculos[carro_selecionado])
    carro_obstaculo = pygame.transform.scale(carro_obstaculo, (obstaculo_largura, obstaculo_altura))
    pos_obstaculo_X = random.randrange(0, (LARGURA-obstaculo_largura))
    pos_obstaculo_Y = 0
    obstaculos.append({'imagem':carro_obstaculo, 'eixo_X':pos_obstaculo_X, 'eixo_Y':pos_obstaculo_Y})

# Verifica se houve uma colisão
def colisao(carro_x, carro_y, carro_largura, carro_altura, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
    if carro_x <= obstaculo_x + obstaculo_largura and carro_x + carro_largura >= obstaculo_x and carro_y <= obstaculo_y + obstaculo_altura and carro_y + carro_altura >= obstaculo_y:
        return True
    return False


# Loop do jogo
pontuacao = 0
rodando = True
while rodando:
    #tela.fill((0, 0, 0))  # Limpa a tela
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


    keys = pygame.key.get_pressed()

    # Para garantir que o carro se mantenha entre as faixas brancas da pista

    if keys[pygame.K_LEFT] and keys[pygame.K_SPACE] and x > 50:
        x -= 7
    if keys[pygame.K_RIGHT] and keys[pygame.K_SPACE] and x < 875:
        x += 7
    
    # Move o carro para próximo do meio no eixo Y
    if keys[pygame.K_SPACE] and y < ALTURA and y > 270:
        y -= 0.5
        # obstaculo_velocidade += 0.1
        # Movendo a pista para baixo
        pista_y1 += velocidade_pista
        pista_y2 += velocidade_pista
    else:
        obstaculo_velocidade -= 0.1

    # Mantém o carro em movimento
    if keys[pygame.K_SPACE]:
        obstaculo_velocidade += 0.1
        # Movendo a pista para baixo
        pista_y1 += velocidade_pista
        pista_y2 += velocidade_pista
    else:
        obstaculo_velocidade -= 0.1

    # Acelera o carro
    if keys[pygame.K_UP]:
        obstaculo_velocidade += 0.1
        velocidade_pista += 5
    # Freia o carro
    if keys[pygame.K_DOWN]:
        obstaculo_velocidade += 0.1
        velocidade_pista -= 5
    
    # Reposiciona a pista quando sair da tela
    if pista_y1 >= ALTURA:
        pista_y1 = -ALTURA
    if pista_y2 >= ALTURA:
        pista_y2 = -ALTURA

    # Atualiza obstáclos
    for obstaculo in obstaculos:
        obstaculo['eixo_Y'] += obstaculo_velocidade
    
    # Se sair da tela, reposiciona
        if obstaculo['eixo_Y'] > ALTURA:
            pontuacao += 10
            # Evita que os carros sejam gerados na mesma posião no eixo Y e fora das faixas da pista
            obstaculo['eixo_Y'] = random.randint(-600, -100)
            obstaculo['eixo_X'] = random.randint(50, 890)  

    # Verifica se houve uma colisão
    if colisao(x, y, carro_largura, carro_altura, obstaculo['eixo_X'], obstaculo['eixo_Y'], obstaculo_largura, obstaculo_altura):
        rodando = False

    # Desenha a pista na tela
    tela.blit(pista, (0, pista_y1))
    tela.blit(pista, (0, pista_y2))

    # Desenha o carro na pista
    tela.blit(carro, (x, y))

    # Renderiza os obstáculos
    for obstaculo in obstaculos:
        tela.blit(obstaculo['imagem'], (obstaculo['eixo_X'], obstaculo['eixo_Y']))

    # Renderiza pontuação
    texto = fonte.render('Pontos : '+str(pontuacao), True, (255, 0, 0))
    tela.blit(texto, (50, 50))

    # Atualiza a tela
    pygame.display.update()

    # Controla a taxa de atualização
    pygame.time.delay(30)

pygame.quit()
