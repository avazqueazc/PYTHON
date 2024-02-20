'''if ballrect.bottom > ventana.get_height():#Comprueba si has perdido al tocar el fondo
        gameover = pygame.image.load("Game Over.jpg").convert_alpha()#Convierte la imagen en la pantalla
        gameover = pygame.transform.scale(imagen_perder, (640, 480))#Da el tamaño de la ventana a la imagen
        ventana.blit(gameover, (0, 0))#Son las coordenadas donde inserta la imagen'''