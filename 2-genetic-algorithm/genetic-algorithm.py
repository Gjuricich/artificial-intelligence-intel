'''
Desarrollar un programa que le pida un usuario una palabra de cuatro letras y la adivine por medio de un algoritmo genético. Para ello:

1. Importar la función choice de la librería random.
2. Importar la función fuzz de la librería fuzzywuzzy (previamente instalada desde CMD)
3. Declarar una lista con todos los caracteres el abecedario.
4. Pedirle al usuario que ingrese una palabra de cuatro caracteres. En caso que ingrese un largo incorrecto pedírselo nuevamente.
5. Desarrollar el algoritmo genético para intentar acercarse lo más posible al resultado.'''

import random
from random import choice
import fuzzywuzzy
from fuzzywuzzy import fuzz
import random
from random import choice
import fuzzywuzzy
from fuzzywuzzy import fuzz

alphabet = ["a", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

poblacion = 50
seleccion = 2
generaciones = 100


def ingresarPalabra():
    while True:
        pin = input("Ingrese una palabra (sin espacios): ").lower().strip()
        if ' ' in pin:
            print("Error: La palabra no debe contener espacios.")
        elif len(pin) == 0:
            print("Error: No se ingresó una palabra.")
        else:
            return pin

def genInicial(pin):
    palabras = []
    for i in range(poblacion):
        palabra = []
        for j in range(len(pin)):
            letra = choice(alphabet)
            palabra.append(letra)
        palabra = ''.join(palabra)  
        palabras.append(palabra)
    #print(palabras)
    return palabras


#Devuelve la suma de las coincidencias en la posición y letra entre dos palabras 
def posicionExacta(palabraA, palabraB):
    return sum(1 for c1, c2 in zip(palabraA, palabraB) if c1 == c2)

#Mide el número de posiciones en las que dos cadenas de igual longitud difieren
#cuando la diferencia es mayor, mayor será el número que retorne la suma
def distanciaHamming(palabraA, palabraB):
    return sum(c1 != c2 for c1, c2 in zip(palabraA, palabraB))


def seleccionar(palabras, pin): 
    seleccionados = []
    for i in range(seleccion):
        max_aptitud = 0
        seleccionado = ""
        for j in palabras:
            coincidencia =0.4 * fuzz.ratio(j, pin) + 0.5 * posicionExacta(j, pin) - 0.1 * distanciaHamming(j,pin)
            if coincidencia > max_aptitud:
                max_aptitud = coincidencia
                seleccionado = j  
        seleccionados.append(seleccionado)  
        palabras = [palabra for palabra in palabras if palabra != seleccionado]
    #print("seleccionados: ", seleccionados)
    return seleccionados

def heredar(seleccionados, pin, cantGeneraciones):
    nuevaGeneracion = []
    for _ in range(poblacion):
        palabra = ""
        for i in range(len(pin)):
            if (random.random() < 0.1) & (cantGeneraciones < 90):  
                 palabra += seleccionados[random.randint(0, 1)][i]  
            elif (random.random() < 0.5) & (cantGeneraciones > 10):
                 palabra += seleccionados[random.randint(0, 1)][i]
            else:
                 palabra += choice(alphabet)  
        nuevaGeneracion.append(palabra)
    return nuevaGeneracion


def main():
    pin = ingresarPalabra()
    seleccionados = []   
    palabras = genInicial(pin)
    cantGeneraciones = 0
    for i in range(generaciones - 1):
        seleccionados = seleccionar(palabras, pin)
        palabras = heredar(seleccionados,pin,cantGeneraciones)
        cantGeneraciones += 1
    
    seleccionFinal = seleccionar(palabras, pin)  
    print(seleccionFinal)
    palabraA = 0.5 * fuzz.ratio(seleccionFinal[0], pin) + 0.5 * posicionExacta(seleccionFinal[0], pin)
    palabraB = 0.5 * fuzz.ratio(seleccionFinal[1], pin) + 0.5 * posicionExacta(seleccionFinal[1], pin)
    
    if palabraA > palabraB:
        print("La palabra que más se aproxima a la ingresada es: ", seleccionFinal[0])
    else:
        print("La palabra que más se aproxima a la ingresada es: ", seleccionFinal[1])

main()
