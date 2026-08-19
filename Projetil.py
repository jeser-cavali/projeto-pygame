import pygame.draw

from ElementoJogo import ElementoJogo


class Projetil(ElementoJogo):
    def __init__(self, x, y, velocidade=10, cor=(0, 0, 0)):
        super().__init__(
            x = x,
            y = y,
            largura = 0,
            altura = 0,
            cor = cor,
            velocidade = velocidade
        )
        self.isVisible = 1

    def mover(self):
        self.rect.y -= self.velocidade

        if self.rect.y < 0:
            self.isVisible = 0

    def atualizar(self):
        self.mover()

    def desenhar(self, tela):
        if self.isVisible == 1:
            pygame.draw.circle(tela, (255, 255, 255), (self.rect.x, self.rect.y), 5)


