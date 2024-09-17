import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#######################################################################
#                             Funciones                               #
#######################################################################

def limpiar_consola():
    os.system('cls')
    
def mostrar_menu():
    print("")
    print("----------------------------------------")
    print("Bienvenido al menú del Ejercicio Datos 1")
    print("")
    print("1 - Ver todos los jugadores")
    print("2 - Ver detalle por jugador")
    print("3 - Ver puntaje general")
    print("4 - Ver gráfico de puntajes")
    print("0 - Salir")

def cargar_csv(nombre):
    df=pd.read_csv(nombre)
    df=df.rename(columns={"nombre":"jugador"})
    return df

def mostrar_todos(df):
    for i in df.jugador:                               
     print("  - " + i) 

def ver_detalle(df): 
    nombre = input("Ingrese el nombre del jugador: ").strip().lower()  
    jugador_detalle = (df[df.jugador == nombre])  
    if jugador_detalle.empty:
        print("  - El ingresado jugador no existe.")
    else:
        print(jugador_detalle)

def puntaje_general(df):
    tam = len(df)
    acu=0
    for i in df.puntos:
     acu+=i

    print("  - Puntaje general: " + str(acu/tam))



    for jugador in df['Jugador']:
        if nombre in contador:
            contador[nombre] += 1
            nuevo_nombre = f"{nombre}_{contador[nombre]}"
        else:
            contador[nombre] = 0
            nuevo_nombre = nombre
        nombres_renombrados.append(nuevo_nombre)

    df['Nombre'] = nombres_renombrados


def graficar(df):
    none(df)
    x=df.jugador
    y=df.puntos  
    plt.figure(figsize=(10 , 10)) 
    plt.bar(x , y , color="green")   
    plt.xlabel("Jugador")   
    plt.ylabel("Puntaje")  
    plt.title("Puntaje por jugador (nba)")   
    plt.show()

def main(nombre):
    df = cargar_csv(nombre)
    salir = False
    while not salir:
        limpiar_consola()  
        mostrar_menu()
        opcion = input("  Ingrese una opción (1-2-3-4-0): ")
        print("")
        match opcion:
            case '1':
                print("Jugadores")
                mostrar_todos(df)
            case '2':
                print("Detalle jugador")
                ver_detalle(df)
            case '3':
                print("Puntaje general")
                puntaje_general(df)
            case '4':
                print("Gráfico Jugadores")
                graficar(df)
            case '0':                
                salir=True
                print("Opción elegida: Salir")
            case _:        
                print("La opción elegida no esta disponible.") 
        input("Presione enter para continuar...")


#Llamado a función principal
main("nba.csv")



    

