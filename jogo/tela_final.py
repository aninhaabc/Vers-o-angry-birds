import pygame

def tela_final(screen):
    # Preenche o fundo com preto
    screen.fill((16,16,73))

    # Carrega as imagens
    gatinho_img = pygame.image.load("jogo/imagens/gatinho_menu.png")
    patinho_img = pygame.image.load("jogo/imagens/patinho_menu.png")

    # Redimensiona as imagens se necessário
    gatinho_img = pygame.transform.scale(gatinho_img, (100, 100))  
    patinho_img = pygame.transform.scale(patinho_img, (100, 100))  

    # Centraliza as imagens na tela
    screen.blit(gatinho_img, ( 195, 150))  
    screen.blit(patinho_img, (275, 150))   

    # Definindo a fonte e os textos
    fonte_titulo = pygame.font.Font("jogo/fonte/minecraftia/Minecraftia-Regular.ttf", 20)

    titulo_texto = fonte_titulo.render("Parabéns você concluiu o objetivo!", True, (255, 255, 255))

    # Centralizando os textos na tela
    screen.blit(titulo_texto, (screen.get_width() // 2 - titulo_texto.get_width() // 2, 50))

    # Atualiza a tela
    pygame.display.flip()

    click = True 
    while click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                click = False
    
    pygame.quit()



