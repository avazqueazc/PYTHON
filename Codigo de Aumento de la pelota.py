'''hit_counter = 0#Contador de golpes con la barra
acceleration_threshold = 3# Aumentar la velocidad de la pelota cada 3 golpes

    if baterect.colliderect(ballrect):#Colisión de la pelota con la barra
        speed[1] = -speed[1]#Modifica el sentido de la bola de las posiciones X, Y
        hit_counter += 1#Suma uno cada vez que la bola haya rebotado 3 veces en la barra
        if hit_counter % acceleration_threshold == 0:#Calcula el multiplo de los golpes asignados
            speed[0] *= 1.2  # Aumentar la velocidad de la pelota'''