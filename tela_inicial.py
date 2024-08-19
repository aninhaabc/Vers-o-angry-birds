import pygame

def tela_inicial(screen):
    # Preenche o fundo com preto
    screen.fill((0, 0, 0))

    # Definindo a fonte e os textos
    fonte_titulo = pygame.font.Font(None, 74)
    fonte_opcao = pygame.font.Font(None, 50)

    titulo_texto = fonte_titulo.render("Patinho vs Gatinho", True, (255, 255, 255))
    iniciar_texto = fonte_opcao.render("Clique para Iniciar", True, (255, 255, 255))

    # Centralizando os textos na tela
    screen.blit(titulo_texto, (screen.get_width() // 2 - titulo_texto.get_width() // 2, 100))
    screen.blit(iniciar_texto, (screen.get_width() // 2 - iniciar_texto.get_width() // 2, 250))

    # Atualiza a tela
    pygame.display.flip()


