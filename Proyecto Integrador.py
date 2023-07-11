#Parte I
#Pedir el nombre del jugador por teclado
#Imprimir un mensaje de bienvenida con el nombre del jugador
nombre_jugador = input("Ingresa tu nombre: ")
print("Bienvenido," + nombre_jugador + "\nDisfruta la partida!")

#Parte II
from readchar import readkey
while True: 
    tecla = readkey()
    if tecla.encode() == b'\x00H': # Código de escape (para salir del bucle infinito)=\x1b[A.
        print("Se presionó la tecla ↑ (flecha hacia arriba)")
        break     
    else:
        print(f"se presionó la tecla: {tecla}")

import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


#Parte III
def main():
    number = 0
    while True:
        clear()
        print(number)
        key = input("Presiona 'n' para continuar o cualquier otra tecla para salir: ")
        if key != 'n':
            break
        number += 1
        if number > 50:
            break

if __name__ == '__main__':
    main()
