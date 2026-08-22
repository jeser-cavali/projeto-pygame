import random
import pygame

class Estrela:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        
        # Tamaño de 1 a 2 píxeles para dar variedad
        self.tamanho = random.randint(1, 2)
        
        # Posición inicial aleatoria (tanto en X como en Y para llenar la pantalla al inicio)
        self.x = random.randint(0, self.largura_tela)
        self.y = random.randint(0, self.altura_tela)
        
        # Velocidad constante rápida
        self.velocidade = 8

    def mover(self):
        self.y += self.velocidade

        # Cuando sale por abajo, reaparece arriba en una posición X aleatoria
        if self.y > self.altura_tela:
            self.y = random.randint(-20, -5)
            self.x = random.randint(0, self.largura_tela)

    def desenhar(self, tela):
        # Dibuja la estrella como un pequeño punto blanco
        pygame.draw.rect(tela, (255, 255, 255), (self.x, self.y, self.tamanho, self.tamanho))