import pygame
import math
from tela_inicial import tela_inicial

# Inicializando pygame
pygame.init()

jogo_iniciado = False

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
# screen.blit(gato2_redimensionado, (270,170))

# Carregando a imagem "gatinho perdendo"
gatinho_perdendo = pygame.image.load('imagens/gatinho_perdendo.png')
gatinho_perdendo_redimensionado = pygame.transform.scale(gatinho_perdendo, (50, 50))

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

# Inicializando o estado dos gatos
gato1_acertado = False
gato2_acertado = False


# Função para desenhar a trajetória pontilhada
def desenhar_trajetoria(screen, start_pos, angle, velocidade_inicial, gravidade):
    num_pontos = 30  # Número de pontos da trajetória
    distancia_entre_pontos = 100  # Aumentando a distância entre pontos
    for i in range(num_pontos):
        # Calculando a posição futura do pato com base no ângulo e velocidade
        t = i * distancia_entre_pontos / 50   
        futuro_x = start_pos[0] + math.cos(angle) * velocidade_inicial * t * 30
        futuro_y = start_pos[1] + math.sin(angle) * velocidade_inicial * t * 30 + 0.5 * gravidade * (t * 30) ** 2

        # Desenhar um pequeno círculo para simular o ponto
        pygame.draw.circle(screen, (255, 255, 255), (int(futuro_x), int(futuro_y)), 3)

# Loop principal
running = True
while running:
    if not jogo_iniciado:
        tela_inicial(screen)  # Chama a função tela_inicial de tela_inicial.py

        # Aguarda o clique do mouse para iniciar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogo_iniciado = True  # Muda o estado para iniciar o jogo
    else:
        # Loop do jogo após a tela inicial
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Detecta o clique do mouse para arremessar
            if event.type == pygame.MOUSEBUTTONDOWN and not pato_lancado:
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

    # Desenhando a trajetória pontilhada antes do lançamento
        if not pato_lancado:
            # Obtendo a posição atual do mouse para desenhar a trajetória
            mouse_x, mouse_y = pygame.mouse.get_pos()
            delta_x = mouse_x - pato_pos[0]
            delta_y = mouse_y - pato_pos[1]
            angulo = math.atan2(delta_y, delta_x)

            # Desenhar a trajetória pontilhada
            desenhar_trajetoria(screen, pato_pos, angulo, 0.5, gravidade)

        # Desenhando os personagens na tela e verificando se o gato foi acertado
        screen.blit(pato_redimensionado,pato_pos)
        if gato1_acertado:
            screen.blit(gatinho_perdendo_redimensionado, gato1_pos)
        else:
            screen.blit(gato1_redimensionado, gato1_pos)

        if gato2_acertado:
            screen.blit(gatinho_perdendo_redimensionado, gato2_pos)
        else:
            screen.blit(gato2_redimensionado, gato2_pos)

        # Retangulo de colisão para o pato e os gatos
        pato_rect = pygame.Rect(pato_pos[0], pato_pos[1], 50, 50)
        gato1_rect = pygame.Rect(gato1_pos[0], gato1_pos[1], 50, 50)
        gato2_rect = pygame.Rect(gato2_pos[0], gato2_pos[1], 50, 50)

        # Verificar colisões
        if colisao(pato_rect, gato1_rect) and not gato1_acertado:
            gato1_acertado = True  
            pato_pos = [50, 300]   
            pato_lancado = False 

        if colisao(pato_rect, gato2_rect) and not gato2_acertado:
            gato2_acertado = True
            pato_pos = [50, 300]   
            pato_lancado = False 

        
        # Atualizando a tela
        pygame.display.flip()

# Encerrando o pygame
pygame.quit()