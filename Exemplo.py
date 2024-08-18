import pygame

class Entidade:
    def __init__(self, sprite_url: str, scale: int) -> None:
        self.sprite = pygame.image.load(sprite_url)
        self.scale = scale

    def desenhar(self, screen, x, y):
        entidade = pygame.transform.scale(self.sprite, (self.scale, self.scale))

        return screen.blit(entidade, (x, y))

class Patinho(Entidade):
    def __init__(self, sprite_url: str, scale: int) -> None:
        self.posicao = (30, 30)
        self.velocidade = (30, 30)
        super().__init__(sprite_url, scale)

    def aceleração(self, x, y):
        self.velocidade[0] += x
        self.velocidade[1] += y

class Gatinho(Entidade):
    def __init__(self, sprite_url: str, scale: int) -> None:
        super().__init__(sprite_url, scale)
    


screen = pygame.display.set_mode((564,443))


gatinho = Gatinho(sprite_url='', scale=50)

patinho = Patinho(sprite_url='imagens/patinho.png', scale=50)
patinho.desenhar(screen, 30, 60)