import pygame

pygame.init()#Inicialización de Pygame

ventana = pygame.display.set_mode((640,480))#Da un tamaño a la ventana
pygame.display.set_caption("Pygame")#Titulo de la ventana

jugando = True#Inicia el juego
while jugando:#Bucle del juego
    
    for event in pygame.event.get():#Comprueba los eventos
        if event.type == pygame.QUIT:#Comprobamos si se ha pulsado el botón de cierre de la ventana
            jugando = False#Cierra el juego despues de haber pulsado la "X"

    fondo = pygame.image.load("cielo.png").convert()#Inserta una imagen de fondo de pantalla
    fondo = pygame.transform.scale(fondo, (640, 480))#Ajusta el tamaño de la imagen al de la pantalla
    ventana.blit(fondo, (0, 0))#Dibuja el fondo en la pantalla

    pygame.display.flip()#Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60)#Controlador de frecuencia de refresco(FPS)

pygame.quit()
