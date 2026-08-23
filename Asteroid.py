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
        self.sprites = [
            pygame.transform.scale(pygame.image.load('./media/Sprite-0002.png').convert_alpha().subsurface((0, 0, 32, 32)), (64, 64)),
            pygame.transform.scale(pygame.image.load('./media/Sprite-0002.png').convert_alpha().subsurface((32, 0, 32, 32)),(64, 64)),
            pygame.transform.scale(pygame.image.load('./media/Sprite-0002.png').convert_alpha().subsurface((64, 0, 32, 32)),(64, 64)),
        ]
        self.hits = 0
        self.random_angle = random.randint(0, 359)

    def iniciar_status(self):
        # 1. Posición X aleatoria dentro de la pantalla
        limite_x = max(0, self.largura_tela - self.rect.width)
        self.rect.x = random.randint(0, limite_x)

        # 2. Posición Y aleatoria arriba de la pantalla (fuera de vista)
        self.rect.y = random.randint(-150, -50)

        # 3. Velocidad aleatoria de caída
        self.velocidade = random.randint(3, 7)

        self.hits = 0

    def modularVelocidade(self, condition: bool):
        if condition:
            self.velocidade = 10
        else:
            self.velocidade = 5


    def mover(self):
        self.rect.y += self.velocidade

        # Reinicia arriba si pasa el borde inferior de la pantalla
        if self.rect.top > self.altura_tela:
            self.iniciar_status()

    def desenhar(self, tela):
        # Dibuja el asteroide como un círculo rojo
        if self.rect.y <= self.altura_tela:
            tela.blit(pygame.transform.rotate(self.sprites[self.hits], self.random_angle), (self.rect.x - 32, self.rect.y - 32))
            #pygame.draw.circle(tela, self.cores[self.hits], self.rect.center, self.raio)