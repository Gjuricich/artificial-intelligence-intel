import cv2
import random

'''
Realizar un bucle que muestre aleatoriamente una de las tres imágenes de los semáforos adjuntos por intervalos de 2 segundos.
En cada vuelta el sistema deberá reconocer el estado del semáforo e imprimir según corresponda:
Semáforo en rojo! - Detenerse!
Semáforo en amarillo - Atención!
Semáforo en verde - Avanzar!
'''


def cargarImagenes():
    tam = 3
    imgs = []
    for i in range(0,tam):
        img = cv2.imread(str(i+1)+".png")
        img = cv2.resize(img,(355,606))
        imgs.append(img)   
    return imgs

#cant representa la cantidad de veces que las imagenes se van a mostrar
def mostrarImagenes(imgs,cant):
    time = 2000
    for i in range(0,cant):
          index = random.randint(0,2)
          img = imgs[index]
          cv2.imshow("semaforo", img)
          analizarColor(img)
          cv2.waitKey(time)
    cv2.destroyAllWindows()


def analizarColor(img):
    #evalúo tres pixeles
    pixelSuperior = img[202,175]
    pixelMedio = img[360,230]
    pixelInferior= img[550,175]
    
    #extraigo el rgb de cada pixel y analizo cual es el color predominante preguntando si las
    #tres condiciones para cada color se cumplen
    rojo = pixelSuperior[2] > 150 and pixelSuperior[1] < 100 and pixelSuperior[0] < 100
    amarillo = pixelMedio[2] > 150 and pixelMedio[1] > 150 and pixelMedio[0] < 100
    verde = pixelInferior[1] > 150 and pixelInferior[2] < 100 and pixelInferior[0] < 100
    
    #Cuando el color dominante sea true se muestra el mensaje correspondiente
    if rojo:
        print("Semáforo en rojo! - Detenerse!")
    elif amarillo:
        print("Semáforo en amarillo - Atención!")
    elif verde:
        print("Semáforo en verde - Avanzar!")
    else:
        print("No se pudo determinar el estado del semáforo")
     

def main():
    cant = 10
    imgs = cargarImagenes()
    mostrarImagenes(imgs,cant)

main()
