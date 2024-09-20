'''
1. Importar el csv como matriz en python.
2. Eliminar de la matriz a los jugadores que no posean fotos.
3. Imprimir un mensaje indicando aquellos jugadores que posean foto en blanco y negro.
4. Que el programa muestre un menu que le pida al usuario que indique que desea hacer: ver un jugados, ver todos o borrar un jugador.
5. Si selecciona ver un jugador, el sistema le pedirá el número de camiseta y que lo imprima en pantalla con su nombre por como título y sin mostrar los ejes.
6. Si selecciona ver todos, mostrar en una sola impresión a todos los jugadores.
7. Si decide borrar un jugador, pedirle el nombre y el apellido. Borrar su foto de la carpeta y eliminarlo de la matriz. También borrarlo del archivo csv original.'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os 


def mostrar_menu():
    print("")
    print("----------------------------------------")
    print("Bienvenido al menú del Ejercicio Imágenes 1")
    print("")
    print("1 - Ver todos los jugadores")
    print("2 - Ver jugador")
    print("3 - Eliminar jugador")
    print("0 - Salir")

def limpiar_consola():
    os.system('cls')

def cargar_csv(nombre):
    df=pd.read_csv(nombre)
    jugadores = df.to_numpy().tolist()
    return jugadores

def cargar_fotos(ruta):
    fotos= os.listdir(ruta)
    return fotos

def eliminar_jugadores_sin_foto(jugadores, fotos):
    jugadores_con_foto = [
    jugador for jugador in jugadores
       if f"{jugador[2]} {jugador[1]}.jpg" in fotos
    ]

    for jugador in jugadores_con_foto:
        jugador.append(f"{jugador[2]} {jugador[1]}.jpg")

    return jugadores_con_foto

def informar_escala(jugadores,ruta):
    jugadores_bn = []
    for jugador in jugadores:
        imagen = mpimg.imread(f"{ruta}/{jugador[3]}")
        if len(imagen.shape) != 3:
            jugadores_bn.append(jugador)
    
    if len(jugadores_bn) != 0:
        print(" ")
        print("Jugadores con foto Blanco y Negro:")
        for j in jugadores_bn:
            print("- " + j[2] + " " + j[1])
        
def mostrar_todos(jugadores,ruta):
    tam = len(jugadores)
    if tam % 2 != 0:
       tam += 1

    n = int(tam/2)
    m = int(tam/n)
    pos = 1
    
    for jugador in jugadores:   
        plt.subplot(m,n,pos)
        foto = mpimg.imread(f"{ruta}/{jugador[3]}")
        plt.imshow(foto)
        plt.axis("off") 
        pos += 1

    plt.suptitle("Selección Argentina")  
    plt.show()


def ver_jugador(jugadores,ruta):
     numero = input("Ingrese el número de camiseta del jugador: ").strip().lower()  
     jugador = next((jugador for jugador in jugadores if jugador[0] == numero), None)
 
     if jugador is None:
        print("  - El ingresado jugador no existe.")
     else:
         foto = mpimg.imread(f"{ruta}/{jugador[3]}")
         plt.imshow(foto)
         plt.title(jugador[2])
         plt.axis("off")
         plt.show()




def eliminar_jugador(nombre_archivo,jugadores,ruta):  
       
     nombre = input("Ingrese el nombre del jugador: ").strip().lower()
     apellido = input("Ingrese el apellido del jugador: ").strip().lower()
     df=pd.read_csv(nombre_archivo)
     jugador = df[(df.nombre == nombre) & (df.apellido == apellido)] 
     jugador_matriz = next((jugador for jugador in jugadores if jugador[2] == nombre and jugador[1] == apellido), None)
     if jugador.empty:
        print("  - El ingresado jugador no existe.")
     else:
        fila = jugador.index
        df.drop(fila, axis=0, inplace=True)
        df.to_csv(nombre_archivo, index=False)
        jugadores = [j for j in jugadores if j[2] != nombre or j[1] != apellido]
        os.remove(f"{ruta}/{jugador_matriz[3]}")
        print("--- El jugador " + nombre + " " + apellido + "ha sido eliminado exitosamente.")
     return jugadores


        

def main(nombre,ruta):
    jugadores = cargar_csv(nombre)
    fotos = cargar_fotos(ruta)
    jugadores = eliminar_jugadores_sin_foto(jugadores,fotos)
    informar_escala(jugadores,ruta)
    salir = False
    print(" ")
    input("Presione enter para abrir el menú...")
    while not salir:
        limpiar_consola()  
        mostrar_menu()
        opcion = input("  Ingrese una opción (1-2-3-0): ")
        print("")
        match opcion:
            case '1':
                print("Jugadores")
                mostrar_todos(jugadores,ruta)
            case '2':
                print("Detalle jugador")
                ver_jugador(jugadores,ruta)
            case '3':
                print("Eliminar jugador")
                jugadores = eliminar_jugador(nombre,jugadores,ruta)
            case '0':                
                salir=True
                print("Opción elegida: Salir")
            case _:        
                print("La opción elegida no esta disponible.") 
        input("Presione enter para continuar...")



#Llamado a función principal


main("argentina.csv", "C:\\Users\\Daniel\\Desktop\\Curso AI INTEL\\3 - Imagenes\\fotos")



