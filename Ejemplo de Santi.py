import pygame
from random import randint
"""inicio"""
pygame.init()
ventana = pygame.display.set_mode((640, 500))
pygame.display.set_caption("ARKANOID")
fondo = pygame.image.load("cielo.png")
fondo = pygame.transform.scale(fondo, (640, 500))
fondorect = fondo.get_rect()
"""pelota"""
ball = pygame.image.load("ball mario.png")
ballrect = ball.get_rect()
speed = [randint(4, 4), randint(4, 4)]
ballrect.move_ip(240, 350)
"""bate"""
bate = pygame.image.load("bate mario.png")
baterect = bate.get_rect()
baterect.move_ip(240, 450)


fuente = pygame.font.Font(None, 36)


"""bloques ladrillos"""
ladrillo_width = 80
ladrillo_height = 20
ladrillos = []
for i in range(5):
    for col in range(10):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        ladrillo = pygame.Rect(col * ladrillo_width, i * ladrillo_height, ladrillo_width, ladrillo_height)
        ladrillos.append((ladrillo, color))


jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    """movimiento"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-8, 0)
       
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(8, 0)


    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
       
    ballrect = ballrect.move(speed)




    """colisiones"""
    for ladrillo, color in ladrillos:
        if ballrect.colliderect(ladrillo):
            ladrillos.remove((ladrillo, color))
            speed[1] = -speed[1]
            speed[0] *= 1.05
            speed[1] *= 1.05
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 200, 200))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.blit(fondo, fondorect)
        ventana.blit(ball, ballrect)
        ventana.blit(bate, baterect)
     
        """bloques restantes"""
        for ladrillo, color in ladrillos:
            pygame.draw.rect(ventana, color, ladrillo)


    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()