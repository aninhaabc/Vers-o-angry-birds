import pygame 
from pathlib import Path
import os

def tela_inicial(screen):

    script_path = Path(os.path.abspath(__file__))
    parent_path = script_path.parent
    # Preenche o fundo com preto
    screen.fill((16,16,73))

    # Carrega as imagens
    gatinho_img = pygame.image.load(parent_path / "assets/imagens/gatinho_menu.png")
    patinho_img = pygame.image.load(parent_path / "assets/imagens/patinho_menu.png")
    botao_play_img = pygame.image.load(parent_path / "assets/imagens/botao_de_play.png")

    # Redimensiona as imagens se necessário
    gatinho_img = pygame.transform.scale(gatinho_img, (100, 100))  
    patinho_img = pygame.transform.scale(patinho_img, (100, 100))  
    botao_play_img = pygame.transform.scale(botao_play_img, (200, 100))  

    # Centraliza as imagens na tela
    screen.blit(gatinho_img, ( 195, 150))  
    screen.blit(patinho_img, (275, 150))   
    screen.blit(botao_play_img, (180, 250))  

    # Definindo a fonte e os textos
    fonte_titulo = pygame.font.Font(parent_path / "assets/fonte/minecraftia/Minecraftia-Regular.ttf", 30)

    titulo_texto = fonte_titulo.render("Patinho vs Gatinho", True, (255, 255, 255))

    # Centralizando os textos na tela
    screen.blit(titulo_texto, (screen.get_width() // 2 - titulo_texto.get_width() // 2, 50))

    # Atualiza a tela
    pygame.display.flip()



