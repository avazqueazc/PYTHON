import pygame
import randint

class Ladrillo(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (60, 20))  # Ajusta el tamaño de los ladrillos
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self._roto = False

    @property
    def roto(self):
        return self._roto

    @roto.setter
    def roto(self, value):
        self._roto = value

    def romper(self):
        self.roto = True

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Pygame")

ball = pygame.image.load("ball mario.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed = [10, -10]  # Cambia la dirección de movimiento de la bola para que vaya hacia arriba
ballrect.move_ip(0, 400)  # Ajusta la posición inicial de la bola debajo de los ladrillos

bate = pygame.image.load("bate mario.png")
bate = pygame.transform.scale(bate, (100, 30))
baterect = bate.get_rect()
baterect.move_ip(270, 450)

ladrillos = []
ladrillo_width = 60
ladrillo_height = 20
columns = 10
rows = 3  # Añade dos filas más de ladrillos
horizontal_gap = 5
vertical_gap = 10  # Espacio entre filas de ladrillos
total_width = columns * (ladrillo_width + horizontal_gap)
x_offset = (ventana.get_width() - total_width) // 2
y_offset = 10  # Ajusta la posición vertical de los ladrillos en la parte superior de la ventana

for row in range(rows):
    for column in range(columns):
        x = x_offset + column * (ladrillo_width + horizontal_gap)
        y = y_offset + row * (ladrillo_height + vertical_gap)
        ladrillo = Ladrillo("ladrillo.png", x, y)
        ladrillos.append(ladrillo)

hit_counter = 0
acceleration_threshold = 3

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-20, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(20, 0)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    for ladrillo in ladrillos:
        if not ladrillo.roto and ballrect.colliderect(ladrillo.rect):
            ladrillo.romper()
            speed[1] = -speed[1]
            break

    if ballrect.colliderect(baterect):
        speed[1] = -speed[1]

    fondo = pygame.image.load("cielo.png").convert()
    fondo = pygame.transform.scale(fondo, (640, 480))

    ventana.blit(fondo, (0, 0))
    
    for ladrillo in ladrillos:
        if not ladrillo.roto:
            ventana.blit(ladrillo.image, ladrillo.rect)

    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)

    if ballrect.bottom > ventana.get_height():
        gameover = pygame.image.load("Game Over.jpg").convert_alpha()
        gameover = pygame.transform.scale(gameover, (640, 480))
        ventana.blit(gameover, (0, 0))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()