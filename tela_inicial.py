import pygame
import math

# Inicializando pygame
pygame.init()

# Configurando a tela
screen = pygame.display.set_mode((564,443))
pygame.display.set_caption("Patinho vs gatinho")

# Carregando a imagem de fundo
background = pygame.image.load('imagens/fundo.jpg')

# Carregando o personagem pato
pato = pygame.image.load('imagens/patinho.png')
pato_redimensionado = pygame.transform.scale(pato, (50, 50))

# Carregando o personagem gato 1 e 2
gato1 = pygame.image.load('imagens/gatinho_sentado.png')
gato1_redimensionado = pygame.transform.scale(gato1,(50,50))
screen.blit(gato1_redimensionado, (270,170))

gato2 = pygame.image.load('imagens/gatinho_sentado.png')
gato2_redimensionado = pygame.transform.scale(gato2,(50,50))
screen.blit(gato2_redimensionado, (270,170))

# Definindo posições dos gatinhos
gato1_pos = [270,178]
gato2_pos = [420,102]

# Definindo variáveis para o pato
pato_pos = [50, 300]  
pato_vel = [0, 0]     
pato_lancado = False  

# Definindo a gravidade
gravidade = 0.0005

# Função para verificar colisão
def colisao(pato_rect, gato_rect):
    return pato_rect.colliderect(gato_rect)
import time
# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detecta o clique do mouse para arremessar
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do clique
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Calcula o vetor de arremesso (diferença entre pato e posição do clique)
            delta_x = mouse_x - pato_pos[0]
            delta_y = mouse_y - pato_pos[1]

            # Calcula a magnitude da velocidade (baseado na distância do clique)
            velocidade_inicial = 0.5

            # Normaliza o vetor e define a velocidade inicial
            angulo = math.atan2(delta_y, delta_x)
            pato_vel[0] = math.cos(angulo) * velocidade_inicial
            pato_vel[1] = math.sin(angulo) * velocidade_inicial

            # Marca que o pato foi lançado
            pato_lancado = True

    # Atualizando a posição do pato se ele foi lançado
    if pato_lancado:
        # Aplica a gravidade no eixo Y
        pato_vel[1] += gravidade

        # Atualiza a posição do pato com base na velocidade
        pato_pos[0] += pato_vel[0]
        pato_pos[1] += pato_vel[1]
 
        # Verifica se o pato saiu da tela e reseta
        if pato_pos[1] > 443 or pato_pos[0] > 564:
            pato_pos = [50, 300]
            pato_vel = [0, 0]
            pato_lancado = False
    # Desenhando a imagem de fundo
    screen.blit(background, (0, 0))

    # Desenhando os personagens na tela
    screen.blit(pato_redimensionado,pato_pos)
    screen.blit(gato1_redimensionado, (270,178))
    screen.blit(gato2_redimensionado, (420,102))

    # Retangulo de colisão para o pato e os gatos
    pato_rect = pygame.Rect(pato_pos[0], pato_pos[1], 50, 50)
    gato1_rect = pygame.Rect(gato1_pos[0], gato1_pos[1], 50,50)
    gato2_rect = pygame.Rect(gato2_pos[0], gato2_pos[1], 50, 50)

    # Atualizando a tela
    pygame.display.flip()

# Encerrando o pygame
pygame.quit()