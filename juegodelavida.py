import copy, random, sys, time

# Ancho de la cuadrícula
ancho = int(input('Introduce el Ancho de la cuadricula del juego: '))
# Alto de la cuadrícula
alto = int(input('Introduce el Alto de la cuadricula del juego: '))

# Carácter para la celda viva
vivo = input('Introduce un caráter que represente la célula viva: ')
# Carácter para la celda muerta
muerto = input('Introduce un caráter que represente la célula muerta: ')

# Las variables celulas y siguientesCelulas son diccionarios que contienen
# el estado actual del juego y el siguiente.
# Las claves del diccionario son tuplas que pueden tener el valor VIVO o MUERTO
siguientesCelulas = {}

# Asignamos valores aleatorios a las células iniciales
for x in range(ancho):
    for y in range(alto):
        # 50% de posibilidades de estar viva o muerta
        if random.randint(0, 1) == 0:
            siguientesCelulas[(x, y)] = vivo
        else:
            siguientesCelulas[(x, y)] = muerto

while True:  # bucle principal del programa
    # Cada iteración de este bucle es una generación de la simulación del juego de la vida

    print('\n' * 50)  # Separación entre generaciones
    celulas = copy.deepcopy(siguientesCelulas)

    # Imprimimos las células por pantalla
    for y in range(alto):
        for x in range(ancho):
            print(celulas[(x, y)], end='')
        print()
    print('Pulsa Ctrl-C para parar.')

    # Calculamos la nueva generación de células en función de los valores actuales
    for x in range(ancho):
        for y in range(alto):
            # Obtenemos las coordenadas de las vecinas incluso si están en el límite
            izquierda = (x - 1) % ancho
            derecha = (x + 1) % ancho
            arriba = (y - 1) % alto
            abajo = (y + 1) % alto

            # Calculamos el número de células vecinas vivas
            numVecinasVivas = 0
            if celulas[(izquierda, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(x, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, arriba)] == vivo:
                numVecinasVivas += 1
            if celulas[(izquierda, y)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, y)] == vivo:
                numVecinasVivas += 1
            if celulas[(izquierda, abajo)] == vivo:
                numVecinasVivas += 1
            if celulas[(x, abajo)] == vivo:
                numVecinasVivas += 1
            if celulas[(derecha, abajo)] == vivo:
                numVecinasVivas += 1

            # Basamos el valor de la nueva generación en función
            # de los valores actuales
            if celulas[(x, y)] == vivo and (numVecinasVivas == 2
                                            or numVecinasVivas == 3):
                # Cálulas vivas con 2 o 3 vecinas vivas permanecen vivas
                siguientesCelulas[(x, y)] = vivo
            elif celulas[(x, y)] == muerto and numVecinasVivas >= 2:
                # Células muertas con 2 o más vecinas vivas cobran vida
                siguientesCelulas[(x, y)] = vivo
            else:
                # En cualquier otro caso continuan muertas
                siguientesCelulas[(x, y)] = muerto

    try:
        time.sleep(1)  # Añadimos un segundo de pausa para evitar parpadeos
    except KeyboardInterrupt:
        print("Juego de la vida de Conway")
        print("https://es.wikipedia.org/wiki/Juego_de_la_vida")
        sys.exit()  # Cuando se pulsa CTRL+C termina el programa
