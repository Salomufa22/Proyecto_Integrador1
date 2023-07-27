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


#Parte III
import os

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    number = 0
    while number <= 50:
        key = input("Presiona 'n' para continuar...")
        if key == 'n':
            clear_terminal()
            print(number)
            number += 1
main()

#Parte IV
lab = """..###################
..#.............#.#.#
#.#######.#####.#.#.#
#...........#.....#.#
#.###.#.#.#.###.###.#
#.#.#.#.#.#.#.....#.#
#.#.#.#####.#####.#.#
#.#.......#.....#...#
#####.###.#####.###.#
#.#.....#.#.#.....#.#
#.#.#####.#.#####.#.#
#.....#.......#.#.#.#
###########.#.#.#####
#.#.......#.#.....#.#
#.#######.#.#.###.#.#
#...#.#.....#.#.#...#
#.###.#.#.###.#.#.#.#
#...#...#.#.#.#.#.#.#
###.###.###.###.###.#
#.......#...........#
###################.#"""
matriz = []
for linea in lab.split("\n"):
    matriz.append(list(linea))
print(matriz)