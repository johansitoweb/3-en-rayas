def tres_en_raya():  
    tablero = [' ' for _ in range(9)]  
    
    def imprimir_tablero():  
        print('-------------')  
        for i in range(3):  
            print(f"| {tablero[i*3]} | {tablero[i*3+1]} | {tablero[i*3+2]} |")  
            print('-------------')  

    def chequear_ganador(jugador):  
        combinaciones_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8),   
                                    (0, 3, 6), (1, 4, 7), (2, 5, 8),   
                                    (0, 4, 8), (2, 4, 6)]  
        return any(all(tablero[i] == jugador for i in combinacion) for combinacion in combinaciones_ganadoras)  

    turno = 'X'  
    for _ in range(9):  
        imprimir_tablero()  
        posicion = int(input(f"Jugador {turno}, elige una posición (0-8): "))  
        
        if tablero[posicion] == ' ':  
            tablero[posicion] = turno  
            if chequear_ganador(turno):  
                imprimir_tablero()  
                print(f"¡Jugador {turno} gana!")  
                return  
            turno = 'O' if turno == 'X' else 'X'  
        else:  
            print("Esa posición ya está ocupada. Intenta de nuevo.")  

    imprimir_tablero()  
    print("¡Es un empate!")  

# Ejecuta el juego  
tres_en_raya()