import pygame

class Ladrillo1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._image = pygame.image.load("ladrillos.png").convert_alpha()  # Cargar imagen del ladrillo 1
        self._rect = self._image.get_rect(topleft=(x, y))

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    def update(self):
        if self.rect.colliderect(ballrect):
            self.kill()

class Ladrillo2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._image = pygame.image.load("ladrillo2.png").convert_alpha()  # Cargar imagen del ladrillo 2
        self._rect = self._image.get_rect(topleft=(x, y))
        self._broken = False

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def broken(self):
        return self._broken

    @broken.setter
    def broken(self, value):
        self._broken = value

    def update(self):
        if self.rect.colliderect(ballrect) and not self.broken:
            self.image = pygame.image.load("ladrillo2_broken.png").convert_alpha()  # Cambiar imagen al ladrillo roto
            self.broken = True
        elif self.broken and self.rect.colliderect(ballrect):
            pass

class Ladrillo3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self._image = pygame.image.load("ladrillo3.png").convert_alpha()  # Cargar imagen del ladrillo 3
        self._rect = self._image.get_rect(topleft=(x, y))

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    def update(self):
        pass

# Aquí empieza el código del juego

pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame")

ball = pygame.image.load("ball mario.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
speed = [8, 8]
ballrect.move_ip(0, 0)

bate = pygame.image.load("bate mario.png")
bate = pygame.transform.scale(bate, (100, 30))
baterect = bate.get_rect()
baterect.move_ip(270, 450)

hit_counter = 0
acceleration_threshold = 3

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-8, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(8, 0)

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        hit_counter += 1
        if hit_counter % acceleration_threshold == 0:
            speed[0] *= 1.5

    fondo = pygame.image.load("cielo.png").convert()
    fondo = pygame.transform.scale(fondo, (640, 480))
    
    ventana.blit(fondo, (0, 0))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()