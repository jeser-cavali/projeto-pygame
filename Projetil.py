import pygame
from ElementoJogo import ElementoJogo

class Projetil(ElementoJogo):
    def __init__(self, x, y, velocidade=12):
        super().__init__(
            x=x - 5,
            y=y,
            largura=10,
            altura=10,
            velocidade=velocidade
        )
        self.isVisible = True
        self.raio = 5

    def mover(self):
        self.rect.y -= self.velocidade

        if self.rect.x < 0:
            self.isVisible = False

    def atualizar(self):
        self.mover()

    def desenhar(self, tela):
        if self.isVisible:
            pygame.draw.circle(tela, (255, 255, 255), self.rect.center, self.raio)