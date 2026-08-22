import random
import pygame
from ElementoJogo import ElementoJogo

class Asteroid(ElementoJogo):
    def __init__(self, largura_tela, altura_tela, velocidade=5, cor=(200, 200, 200)):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.raio = 20

        super().__init__(
            x=0,
            y=0,
            largura=self.raio * 2,
            altura=self.raio * 2,
            cor=cor,
            velocidade=velocidade
        )
        self.iniciar_status()
        self.cores = [
            self.cor,
            (250, 180, 0),
            (200, 0, 0),
            (200, 0, 0)
        ]
        self.hits = 0

    def iniciar_status(self):
        # 1. Posición X aleatoria dentro de la pantalla
        limite_x = max(0, self.largura_tela - self.rect.width)
        self.rect.x = random.randint(0, limite_x)

        # 2. Posición Y aleatoria arriba de la pantalla (fuera de vista)
        self.rect.y = random.randint(-150, -50)

        # 3. Velocidad aleatoria de caída
        self.velocidade = random.randint(3, 7)

        self.hits = 0

    def mover(self):
        self.rect.y += self.velocidade

        # Reinicia arriba si pasa el borde inferior de la pantalla
        if self.rect.top > self.altura_tela:
            self.iniciar_status()

    def desenhar(self, tela):
        # Dibuja el asteroide como un círculo rojo
        if self.rect.y <= self.altura_tela:
            pygame.draw.circle(tela, self.cores[self.hits], self.rect.center, self.raio)