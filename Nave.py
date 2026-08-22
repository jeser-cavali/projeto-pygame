import pygame
import Projetil
from ElementoJogo import ElementoJogo

class Nave(ElementoJogo):
    def __init__(self, largura_tela, altura_tela, velocidade=5, cor=(0, 255, 100)):
        super().__init__(
            x=largura_tela // 2 - 20,
            y=altura_tela - 60,
            largura=40,
            altura=40,
            cor=cor,
            velocidade=velocidade
        )
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.vel_x = 0
        self.tiros = []

        # Intenta cargar imágenes si existen
        try:
            self.sprites = [
                pygame.transform.scale(pygame.image.load('media/Ship-middle.png'), (40, 40)),
                pygame.transform.scale(pygame.image.load('media/Ship-left.png'), (40, 40)),
                pygame.transform.scale(pygame.image.load('media/Ship-right.png'), (40, 40)),
            ]
        except Exception:
            self.sprites = []

        self.current_sprite = 0

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_LEFT, pygame.K_a):
                self.current_sprite = 1
                self.vel_x = -self.velocidade
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                self.current_sprite = 2
                self.vel_x = self.velocidade
            elif evento.key == pygame.K_SPACE:
                self.atirar()

        elif evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_a) and self.vel_x < 0:
                self.current_sprite = 0
                self.vel_x = 0
            elif evento.key in (pygame.K_RIGHT, pygame.K_d) and self.vel_x > 0:
                self.current_sprite = 0
                self.vel_x = 0

    def mover(self):
        self.rect.x += self.vel_x

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela

    def atirar(self):
        # Esta parte la terminará tu compañero en Projetil.py
        self.tiros.append(Projetil.Projetil(self.rect.x + 20, self.rect.y))
        pass

    # TODO Mecânica de tiros
    def atualizar_tiros(self):
        for tiro in self.tiros[:]:
            tiro.atualizar()
            if not tiro.isVisible:
                self.tiros.remove(tiro)

    def atualizar(self):
        self.mover()
        self.atualizar_tiros()

    def desenhar(self, tela):
        if self.sprites:
            tela.blit(self.sprites[self.current_sprite], (self.rect.x, self.rect.y))
        else:
            # Dibuja un triángulo verde si no hay imágenes cargadas
            ponto_topo = (self.rect.centerx, self.rect.top)
            ponto_esq = (self.rect.left, self.rect.bottom)
            ponto_dir = (self.rect.right, self.rect.bottom)
            pygame.draw.polygon(tela, self.cor, [ponto_topo, ponto_esq, ponto_dir])

        for tiro in self.tiros:
            tiro.desenhar(tela)