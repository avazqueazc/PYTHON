import pygame #Importa el módulo pygame
import random #Importa la función randint para generar números aleatorios

class Ladrillo(pygame.sprite.Sprite): #Define la clase Ladrillo
    def __init__(self, image, x, y): #Inicializa la clase Ladrillo 
        self.image = pygame.image.load(image) #Carga la imagen del ladrillo
        self.image = pygame.transform.scale(self.image, (60, 20))  #Ajusta el tamaño de los ladrillos
        self.rect = self.image.get_rect() #Obtengo el rectángulo del ladrillo
        self.rect.x = x #Establece la posición x del ladrillo
        self.rect.y = y #Establece la posición y del ladrillo
        self._roto = False #Establece el estado inicial del ladrillo como no roto

    @property
    def roto(self): #Define un getter para el atributo roto
        return self._roto

    @roto.setter
    def roto(self, value): #Define un setter para el atributo roto
        self._roto = value

    def romper(self): #Define un método para romper el ladrillo
        self.roto = True #Establece el estado del ladrillo como roto

'''Inicio'''
pygame.init() #Inicializar pygame
ventana = pygame.display.set_mode((640,480)) #Da un tamaño a la ventana
pygame.display.set_caption("Pygame") #Titulo de la ventana

'''Musicas'''
pygame.mixer.music.load("Ground Theme.mp3")#Cargar la música de fondo
victoria_sonido = pygame.mixer.Sound("Castle Complete.mp3") #Cargar la música de victoria
derrota_sonido = pygame.mixer.Sound("Game Over.mp3") #Cargar la música de derrota
pygame.mixer.music.play(-1) #Reproducir la música de fondo en bucle

'''Bola'''
ball = pygame.image.load("ball mario.png")#Crea la bola
ball = pygame.transform.scale(ball, (50, 50))#Da un tamaño a la bola
ballrect = ball.get_rect()#Obtengo el rectangulo de la bola
speed = [10, -10] #Da la velocidad de la bola 
ballrect.move_ip(0, 400) #Ajusta la posición inicial de la bola 

'''Bate'''
bate = pygame.image.load("bate mario.png")#Crea el bate 
bate = pygame.transform.scale(bate, (100, 30))#Da un tamaño al bate
baterect = bate.get_rect()#Obtengo el rectangulo de el bate
baterect.move_ip(270, 450)#Las coordenadas de donde aparece el bate

'''Ladrillos'''
ladrillos = [] #Lista de ladrillos
anchura_ladrillo = 60 #La anchura del ladrillo
altura_ladrillo = 20 #La altura del ladrillo
columna = 10 #Añade 10 ladrillos por fila
filas = 3  #Añade 3 filas de ladrillos
hueco_altura = 5 #Espacio entre altura de filas de los ladrillos
hueco_ladrillos = 10  #Espacio entre los ladrillos
anchura_total = columna * (anchura_ladrillo + hueco_altura) #Calcula la anchura total que ocuparan los ladrillos
x_offset = (ventana.get_width() - anchura_total) // 2 # Ajusta la posición horizontal de los ladrillos 
y_offset = 10  # Ajusta la posición vertical de los ladrillos 

for fila in range(filas): #Bucle para generar las filas de ladrillos
    for column in range(columna): # ucle para generar las columnas de ladrillos
        x = x_offset + column * (anchura_ladrillo + hueco_altura) #Calcula la posición x del ladrillo
        y = y_offset + fila * (altura_ladrillo + hueco_ladrillos) #Calcula la posición y del ladrillo
        ladrillo = Ladrillo("ladrillo.png", x, y) #Crea un ladrillo
        ladrillos.append(ladrillo) #Agrega el ladrillo a la lista de ladrillos

'''Mejora de golpes'''
hit_counter = 0 #Contador de golpes con la barra
acceleration_threshold = 5 #Aumenta la velocidad de la pelota cada 5 golpes


jugando = True #Inicia el juego
victoria = False #Establece el inicio del juego como que no has ganado todavia
derrota = False #Establece el inicio del juego como que no has perdido todavia

'''Bucle While'''
while jugando: #Bucle principal del juego
    for event in pygame.event.get(): #Comprueba los eventos
        if event.type == pygame.QUIT: #Comprueba si se ha pulsado el boton de cierre de la pantalla
            jugando = False #Cierra el juego despues de haber pulsado la "X"

    if not victoria and not derrota: #Verifica si has ganado o perdido
        keys = pygame.key.get_pressed() #Compruebo si se ha pulsado alguna tecla
        if keys[pygame.K_LEFT]: #Comprueba si se ha pulsado la tecla (Left)
            baterect = baterect.move(-20, 0) #Da una velocidad al movimiento del bate a la derecha
        if keys[pygame.K_RIGHT]: #Comprueba si se ha pulsado la tecla (Right)
            baterect = baterect.move(20, 0) #Da una velocidad al movimiento del bate a la izquierda

        ballrect = ballrect.move(speed) #Hace que se mueva la bola
        if ballrect.left < 0 or ballrect.right > ventana.get_width(): #Comprueba el limite de la ventana de la parte de los laterales
            speed[0] = -speed[0] #Modifica el sentido de la bola de las posiciones X, Y
        if ballrect.top < 0: #Comprueba el limite de la ventana de la parte superior e inferior
            speed[1] = -speed[1] #Modifica el sentido de la bola de las posiciones X, Y

        for ladrillo in ladrillos: #Bucle for de los ladrillos
            if not ladrillo.roto and ballrect.colliderect(ladrillo.rect): #Comprueba si la bola choca con un ladrillo no roto
                ladrillo.romper() #Rompe el ladrillo
                speed[1] = -speed[1] #Invierte la dirección vertical de la bola despues de chocar
                break

        if ballrect.colliderect(baterect): #Si la pelota con la pelota colisiona con la barra...
            speed[1] = -speed[1] #Modifica el sentido de la bola de las posiciones X, Y
            hit_counter += 1 #Suma uno cada vez que la bola haya rebotado 5 veces en la barra
            if hit_counter % acceleration_threshold == 0: #Calcula el multiplo de los golpes asignados
                speed[0] *= 1.5 #Aumentar la velocidad de la pelota 

        fondo = pygame.image.load("cielo.png").convert() #Inserta una imagen de fondo de pantalla
        fondo = pygame.transform.scale(fondo, (640, 480)) #Ajusta el tamaño de la imagen al de la pantalla

        ventana.blit(fondo, (0, 0)) #Dibuja el fondo en la pantalla

        for ladrillo in ladrillos: #Bucle for de ladrillos
            if not ladrillo.roto: #Si el ladrillo no esta roto...
                ventana.blit(ladrillo.image, ladrillo.rect) #Dibuja el ladrillo en la pantalla

        ventana.blit(ball, ballrect) #Dibuja la bola en la pantalla
        ventana.blit(bate, baterect) #Dibuja el bate en la pantalla

        
        if all(ladrillo.roto for ladrillo in ladrillos): #Comprueba si has roto todos los ladrillos
            pygame.mixer.music.stop() #Para la música de fondo
            victoria_sonido.play() #Reproduce la música de victoria
            victoria = True #Dice que has ganado

        if ballrect.bottom > ventana.get_height(): #Comprueba si la bola ha caído al fondo
            pygame.mixer.music.stop() #Para la musica de fondo
            derrota_sonido.play() #Reproduce la música de derrota
            derrota = True #Dice que has perdido

    elif victoria: #Si ganas
        victoria_image = pygame.image.load("victoria.png") #Convierte la imagen de victoria en la pantalla principal
        victoria_image = pygame.transform.scale(victoria_image, (640, 480)) #Da el tamaño de la ventana a la imagen
        ventana.blit(victoria_image, (0, 0)) #Son las coordenadas donde inserta la imagen

    elif derrota: #Si pierdes
        gameover = pygame.image.load("Game Over.jpg") #Convierte la imagen de derrota en la pantalla principal
        gameover = pygame.transform.scale(gameover, (640, 480)) #Da el tamaño de la ventana a la imagen
        ventana.blit(gameover, (0, 0)) #Son las coordenadas donde inserta la imagen
 
    pygame.display.flip()#Todos los elementos del juego se vuelven a dibujar
    pygame.time.Clock().tick(60)#Controlador de frecuencia de refresco(FPS)

pygame.quit()#Se cierra el programa si salimos del bucle