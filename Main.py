import pygame
from Nave import Nave
from Asteroid import Asteroid
from Estrela import Estrela

# Configuración inicial
pygame.init()
pygame.font.init()  # Inicializar el módulo de fuentes

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
FPS = 60
rodando = True

# Variable de puntos y fuente para la pantalla
pontos = 0
fonte = pygame.font.SysFont("Arial", 26, bold=True)

# Creación de elementos
nave = Nave(LARGURA, ALTURA)

num_asteroides = 5
asteroides = [Asteroid(LARGURA, ALTURA) for _ in range(num_asteroides)]

num_estrelas = 50
estrelas = [Estrela(LARGURA, ALTURA) for _ in range(num_estrelas)]

# Bucle principal del juego
while rodando:
    clock.tick(FPS)

    # 1. Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        nave.processar_evento(evento)

    # 2. Actualización de posiciones
    nave.atualizar()
    
    for estrela in estrelas:
        estrela.mover()

    for asteroide in asteroides:
        asteroide.mover()

    # 3. Verificación de colisiones
    for asteroide in asteroides:
        if nave.rect.colliderect(asteroide.rect):
            print("¡Game Over! La nave fue destruida por un asteroide.")
            rodando = False

    # 4. Dibujo en pantalla
    tela.fill((15, 15, 25))

    # Estrellas de fondo
    for estrela in estrelas:
        estrela.desenhar(tela)

    # Nave y Asteroides
    nave.desenhar(tela)
    for asteroide in asteroides:
        asteroide.desenhar(tela)

    # CONTADOR DE PUNTOS (Esquina superior izquierda)
    texto_pontos = fonte.render(f"PONTOS: {pontos}", True, (255, 255, 255))
    tela.blit(texto_pontos, (20, 20))

    pygame.display.flip()

pygame.quit()