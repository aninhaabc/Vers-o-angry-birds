import pygame

def tela_inicial(screen):
    # Preenche o fundo com preto
    screen.fill((16,16,73))

    # Carrega as jogo/imagens
    gatinho_img = pygame.image.load("jogo/imagens/gatinho_menu.png")
    patinho_img = pygame.image.load("jogo/imagens/patinho_menu.png")
    botao_play_img = pygame.image.load("jogo/imagens/botao_de_play.png")

    # Redimensiona as jogo/imagens se necessário
    gatinho_img = pygame.transform.scale(gatinho_img, (100, 100))  # Exemplo de tamanho
    patinho_img = pygame.transform.scale(patinho_img, (100, 100))  # Exemplo de tamanho
    botao_play_img = pygame.transform.scale(botao_play_img, (200, 100))  # Exemplo de tamanho

    # Centraliza as jogo/imagens na tela
    screen.blit(gatinho_img, ( 195, 150))  
    screen.blit(patinho_img, (275, 150))   
    screen.blit(botao_play_img, (180, 250))  

    # Definindo a fonte e os textos
    fonte_titulo = pygame.font.Font("jogo/fonte/minecraftia/Minecraftia-Regular.ttf", 30)

    titulo_texto = fonte_titulo.render("Patinho vs Gatinho", True, (255, 255, 255))

    # Centralizando os textos na tela
    screen.blit(titulo_texto, (screen.get_width() // 2 - titulo_texto.get_width() // 2, 50))

    # Atualiza a tela
    pygame.display.flip()



