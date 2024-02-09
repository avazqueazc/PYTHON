import pygame

pygame.init()#Inicia pygame
ventana = pygame.display.set_mode((640,480))#Da un tamaño a la ventana
pygame.display.set_caption("Pygame")#Titulo de la ventana

ball = pygame.image.load("ball mario.png")#Crea la bola
ball = pygame.transform.scale(ball, (50, 50))#Da un tamaño a la bola
ballrect = ball.get_rect()#Obtengo el rectangulo de la pelota
speed = [8,8]#Da la velocidad de la bola
ballrect.move_ip(0,0)#Las coordenadas de donde sale la bola

bate = pygame.image.load("bate mario.png")#Crea el bate 
bate = pygame.transform.scale(bate, (100, 30))#Da un tamaño al bate
baterect = bate.get_rect()#Obtengo el rectangulo de el bate
baterect.move_ip(270,450)#Las coordenadas de donde aparece el bate

jugando = True#Inicia el juego
while jugando:#Bucle del juego
    for event in pygame.event.get():#Comprueba los eventos
        if event.type == pygame.QUIT:#Comprueba si se ha pulsado el boton de cierre de la pantalla
            jugando = False#Cierra el juego despues de haber pulsado la "X"

    keys = pygame.key.get_pressed()#Compruebo si se ha pulsado alguna tecla
    if keys[pygame.K_LEFT]:#Comprueba si se ha pulsado la tecla (Left)
        baterect = baterect.move(-8,0)#Da una velocidad al movimiento del bate
    if keys[pygame.K_RIGHT]:#Comprueba si se ha pulsado la tecla (Right)
        baterect = baterect.move(8,0)#Da una velocidad al movimiento del bate

    if baterect.colliderect(ballrect):#Colisión de la pelota con la barra
        speed[1] = -speed[1]#Modifica el sentido de la bola de las posiciones X, Y
    ballrect = ballrect.move(speed)#Hace que se mueva la bola
    if ballrect.left < 0 or ballrect.right > ventana.get_width():#Comprueba el limite de la ventana de la parte de los laterales
        speed[0] = -speed[0]#Modifica el sentido de la bola de las posiciones X, Y
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():#Comprueba el limite de la ventana de la parte superior e inferior
        speed[1] = -speed[1]#Modifica el sentido de la bola de las posiciones X, Y
 
    fondo = pygame.image.load("cielo.png").convert()#Inserta una imagen de fondo de pantalla
    fondo = pygame.transform.scale(fondo, (640, 480))#Ajusta el tamaño de la imagen al de la pantalla
    
    ventana.blit(fondo, (0, 0))#Dibuja el fondo en la pantalla
    ventana.blit(ball, ballrect)#Dibuja la bola en la pantalla
    ventana.blit(bate, baterect)#Dibuja el bate en la pantalla

    pygame.display.flip()#Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60)#Controlador de frecuencia de refresco(FPS)

pygame.quit()#Se cierra el programa si salimos del bucle