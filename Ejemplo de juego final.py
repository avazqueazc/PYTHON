import pygame  # Importa el módulo pygame
from random import randint  # Importa la función randint para generar números aleatorios.


"""inicio"""
pygame.init()  # Inicializa el módulo pygame.
ventana = pygame.display.set_mode((640, 500))  # Crea una ventana de visualización de 640x500 píxeles.
pygame.display.set_caption("ARKANOID")  # Establece el título de la ventana como "ARKANOID".
fondo = pygame.image.load("cielo.png")  # Carga la imagen de fondo del juego.
fondo = pygame.transform.scale(fondo, (640, 500))  # Escala la imagen de fondo al tamaño de la ventana.
fondorect = fondo.get_rect()  # Obtiene el rectángulo que representa el área de la imagen de fondo.



"""pelota"""
ball = pygame.image.load("ball mario.png")  # Carga la imagen de la pelota.
ball = pygame.transform.scale(ball, (40, 40))
ballrect = ball.get_rect()  # Obtiene el rectángulo que representa el área de la pelota.
speed = [randint(4, 4), randint(4, 4)]  # Establece la velocidad inicial de la pelota.
ballrect.move_ip(240, 350)  # Mueve el rectángulo de la pelota a la posición inicial.


"""bate"""
bate = pygame.image.load("bate mario.png")  # Carga la imagen del bate.
bate = pygame.transform.scale(bate, (100, 30))
baterect = bate.get_rect()  # Obtiene el rectángulo que representa el área del bate.
baterect.move_ip(240, 450)  # Mueve el rectángulo del bate a la posición inicial.


fuente = pygame.font.Font(None, 36)  # Crea una fuente para el texto en el juego.


"""bloques ladrillos"""
ladrillo_width = 80  # Ancho de los ladrillos.
ladrillo_height = 20  # Altura de los ladrillos.
ladrillos = []  # Lista para almacenar los ladrillos del juego.
for i in range(5):  # Bucle para crear filas de ladrillos.
    for col in range(10):  # Bucle para crear columnas de ladrillos.
        color = (randint(0, 255), randint(0, 255), randint(0, 255))  # Genera un color aleatorio para cada ladrillo.
        ladrillo = pygame.Rect(col * ladrillo_width, i * ladrillo_height, ladrillo_width, ladrillo_height)  # Crea un rectángulo para un ladrillo.
        ladrillos.append((ladrillo, color))  # Agrega el rectángulo del ladrillo y su color a la lista de ladrillos.


jugando = True  # Variable para controlar el bucle principal del juego.
while jugando:  # Bucle principal del juego.
    for event in pygame.event.get():  # Manejo de eventos del juego.
        if event.type == pygame.QUIT:  # Si se cierra la ventana, el juego termina.
            jugando = False


    """movimiento"""
    keys = pygame.key.get_pressed()  # Obtiene el estado de las teclas presionadas.
    if keys[pygame.K_LEFT]:  # Si se presiona la tecla izquierda, mueve el bate a la izquierda.
        baterect = baterect.move(-8, 0)
    if keys[pygame.K_RIGHT]:  # Si se presiona la tecla derecha, mueve el bate a la derecha.
        baterect = baterect.move(8, 0)
    if baterect.colliderect(ballrect):  # Si hay colisión entre el bate y la pelota, cambia la dirección vertical de la pelota.
        speed[1] = -speed[1]
    ballrect = ballrect.move(speed)  # Mueve la pelota de acuerdo a su velocidad.


    """colisiones"""
    for ladrillo, color in ladrillos:  # Verifica colisiones con los ladrillos y la pelota.
        if ballrect.colliderect(ladrillo):  # Si hay colisión entre la pelota y un ladrillo...
            ladrillos.remove((ladrillo, color))  # Elimina el ladrillo de la lista de ladrillos.
            speed[1] = -speed[1]  # Invierte la dirección vertical de la pelota.
            speed[0] *= 1.05  # Aumenta la velocidad horizontal de la pelota.
            speed[1] *= 1.05  # Aumenta la velocidad vertical de la pelota.
    if ballrect.left < 0 or ballrect.right > ventana.get_width():  # Si la pelota choca contra los bordes laterales de la ventana...
        speed[0] = -speed[0]  # Invierte la dirección horizontal de la pelota.
    if ballrect.top < 0:  # Si la pelota choca contra el borde superior de la ventana...
        speed[1] = -speed[1]  # Invierte la dirección vertical de la pelota.
    if len(ladrillos) == 0:  # Si no quedan ladrillos en el juego...
        texto_ganador = fuente.render("¡Has ganado!", True, (0, 255, 0))  # Mensaje de victoria.
        texto_ganador_rect = texto_ganador.get_rect()  # Obtiene el rectángulo del mensaje de victoria.
        texto_ganador_x = ventana.get_width() / 2 - texto_ganador_rect.width / 2  # Calcula la posición x del mensaje de victoria.
        texto_ganador_y = ventana.get_height() / 2 - texto_ganador_rect.height / 2  # Calcula la posición y del mensaje de victoria.
        ventana.blit(texto_ganador, [texto_ganador_x, texto_ganador_y])  # Dibuja el mensaje de victoria en la ventana.
    elif ballrect.bottom > ventana.get_height():  # Si la pelota cae por debajo del borde inferior de la ventana...
        texto = fuente.render("Game Over", True, (125, 200, 200))  # Mensaje de fin de juego.
        texto_rect = texto.get_rect()  # Obtiene el rectángulo del mensaje de fin de juego.
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2 # Calcula la posición x del mensaje de victoria.
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2 # Calcula la posición y del mensaje de victoria.
        ventana.blit(texto, [texto_x, texto_y]) # Dibuja el mensaje de victoria en la ventana.
    else:
        ventana.blit(fondo, fondorect)  # Mantiene el fondo igual
    ventana.blit(ball, ballrect)  # Mantiene la pelota igual
    ventana.blit(bate, baterect)  # Mantiene el bate igual


    """bloques restantes"""
    for ladrillo, color in ladrillos:  # ladrillos restantes en el juego.
        pygame.draw.rect(ventana, color, ladrillo)  # Mantiene cada ladrillo en su posicion y color.


    pygame.display.flip()  # Actualiza la pantalla.
    pygame.time.Clock().tick(60)  # Controla la velocidad de fotogramas del juego a 60 FPS.


pygame.quit()  # Sale del juego pygame.