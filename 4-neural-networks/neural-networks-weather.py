'''
1. Importa el archivo csv como un dataframe
2. Armar los datasets de entradas y salidas con los valores del dataframe
3. Desarrollar un sistema que le permita el asuario predecir la temperatura de la tierra.
4. Que el sistema se ejecute guardando el modelo entrenado.
'''

import pandas as pd
import numpy as np
import tensorflow as tf
import keras



df=pd.read_csv('clima.csv')
weather = df.to_numpy().tolist()
years = []
temp = []

for w in weather:
    years.append(int(w[0]))
    temp.append(float(w[1]))

years=np.asarray(years)
temp=np.asarray(temp)

layer_1=keras.layers.Dense(units=5,input_shape=[1])
layer_2=keras.layers.Dense(units=5)
layerOut=keras.layers.Dense(units=1)

model=keras.Sequential([layer_1,layer_2,layerOut])
model.compile(optimizer="Nadam" , loss="mean_squared_error")
model.fit(years,temp,epochs=50) 

'''
model.save("modelo.keras")
model=keras.models.load_model("modelo.keras")
'''

year=input("Ingrese el año: ")
yearIn=[int(year)]
yearIn=np.asarray(yearIn)
tempProm = model.predict(yearIn)
print("La temperatura global promedio para el año " + year + " es  de " + str(tempProm) + "°C")
