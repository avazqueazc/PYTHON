# Colisión de la pelota con la barra
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]
        hit_counter += 1
        if hit_counter % acceleration_threshold == 0:
            speed[0] *= 1.2  # Aumentar la velocidad de la pelota


# Contador de golpes con la barra
hit_counter = 0
acceleration_threshold = 5  # Aumentar la velocidad de la pelota cada 3 golpes