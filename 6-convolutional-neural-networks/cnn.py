'''
Normalización de imágenes (resize):
Todas las imágenes tendrán el mismo tamaño para que sean comparables. Luego, se pasan a escala de grises, transformando los píxeles en números (a cada píxel se le asigna un número correspondiente a la escala de gris).

¿Cómo funciona?
La red neuronal convolucional (CNN) toma un píxel y compara su valor numérico con el de su entorno, identificando la diferencia numérica entre ellos. Cuando la diferencia es grande, la red neuronal entiende que existe un alto contraste de color, lo que indica la presencia de una línea de contraste. Este proceso se repite con todos los píxeles, encontrando patrones de líneas y formas a través de operaciones matemáticas.

Capa de entrada:
La capa de entrada de la red neuronal tendrá tantas neuronas como píxeles tenga la imagen.

Capa de salida:
La capa de salida debe tener tantas neuronas como criterios de clasificación se definan (por ejemplo, manzanas y naranjas, dos neuronas).

Capas ocultas:

Convolución: Es el proceso antes mencionado, donde se identifican patrones de líneas y contrastes.
Agrupamiento (Pooling): Esta etapa reconoce los patrones más fuertes y destacados.
Después de la convolución, se obtiene una matriz. El proceso de agrupamiento toma esa matriz, promedia los valores de los píxeles y genera un píxel más grande con el valor promedio. Posteriormente, se vuelve a convolucionar sobre ese agrupamiento, obteniendo capas con píxeles más grandes. Si se siguen encontrando diferencias numéricas entre los píxeles, se continuarán identificando patrones de forma y líneas más marcadas. Luego del agrupamiento, la red neuronal sigue detectando diferencias de contraste.

Importancia del agrupamiento:
El agrupamiento es crucial para que la red neuronal identifique y reconozca cuáles líneas son más importantes, cuáles se mantienen después del proceso de agrupamiento y cuáles no.
'''
import tensorflow as tf
import keras
import numpy as np
import cv2

# -----------------  Automatización de carga y preparación de set de datos ----------------------------

categorias=["manzanas" , "ananas" , "kiwis"]
#Almacena en imagenes la matriz numerica de la escala de grises
imagenes=[]  
#La etiqueta representa la matriz numerica de pixeles de cada tipo de imagen
#por ejemplo, si es manzana en labels = [0,0,0,1,1,1,2,2,2] tres matrizes para tresimagenes de manzanas
labels=[] 
#contador de label
contCategoria=0
for i in categorias: 
    #contador de imagenes por carpeta
    contImagen = 1
    for k in range (10): 
        #almaceno en memoria la imagen en escala de grises "0"
        img=cv2.imread(i+"/"+str(contImagen)+".jpg",0)
        img=cv2.resize(img,(200,200)) 
        img=np.asarray(img)
        imagenes.append(img)
        contImagen=contImagen+1
        labels.append(contCategoria) 
    contCategoria=contCategoria+1 


# -------- Modelo de red neuronal -------------------

model=keras.Sequential([
    #capa de convolución tomas matrices de 3 x 3 px y genera 32 salidas, 200,200 tamaño 1 gris
    keras.layers.Conv2D(32, (3,3), input_shape=(200,200,1), activation="relu"), 
    keras.layers.MaxPooling2D(2,2), #capa de agrupamiento
    keras.layers.Conv2D(64, (3,3), input_shape=(200,200,1), activation="relu"),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Dropout(0.5), #apago el 50% de las neuronas
    keras.layers.Flatten(), 
    keras.layers.Dense(units=100, activation="relu"), #capa oculta de 100 neuronas
    keras.layers.Dense(3, activation="softmax") #capa de salida
])

# ------ Compilación ---------------

model.compile(optimizer="adam",
loss="sparse_categorical_crossentropy", 
metrics=["accuracy"])


imagenes=np.array(imagenes)
labels=np.array(labels)
model.fit(imagenes , labels , epochs=20)

test=cv2.imread("test.jpg",0) 
test=cv2.resize(test,(200,200)) 
test=np.asarray(test)
test=np.array([test]) 


resultado=model.predict(test)
print(resultado) #[[0.8 0.2 0]]   #0
print("Manzana:" , resultado[0][0]*100, "%" )  #80%
print("Anana:" , resultado[0][1]*100 , "%")   #20%
print("Kiwi:" , resultado[0][2]*100 , "%" )   #0%

print("Resultado final: " , categorias[np.argmax(resultado[0])])




