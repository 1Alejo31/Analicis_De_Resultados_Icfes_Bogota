"""
 * @Institución: Iberoamericana de colombia 
 * @authors:  Juan Camilo Hernández Zúñiga <jherna91@ibero.edu.co>,
 * Krhistian Alejandro Gonzalez Duarte <alejo.g31@hotmail.com>,
 * Leindis Dik Monterroza Hernández <Leindish@gmail.com>
 * Fernando Sanchez Romero <fernandosanchezrome@gmail.com>
 * @Proyecto: Analisis De Resultados Icfes Bogota
 * @version: 1.0 [14/08/2023]
"""

"""
 * @Institución: Iberoamericana de colombia 
 * @Proyecto: Importacion de librerias
 * @version: 1.0 [14/08/2023]
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


"""
 * @Institución: Iberoamericana de colombia 
 * @Proyecto: Llamado de la base de datos y leyendo la misma
 * @version: 1.0 [14/08/2023]
"""

url = 'https://raw.githubusercontent.com/it-ces/Datasets/main/icfes.csv'
df = pd.read_csv(url)

"""
 * @Institución: Iberoamericana de colombia 
 * @Proyecto: Veridicando las columnas que posee la base de datos
 * @version: 1.0 [14/08/2023]
"""
print(df.columns)

X = ['PUNT_GLOBAL',  'PUNT_MATEMATICAS', 'PUNT_INGLES',  'PUNT_SOCIALES_CIUDADANAS', 'PUNT_LECTURA_CRITICA' ]

#Creando sub base
#Para ver la correlacion
print(df[X].corr())

df = df[X]

#Para graficar
ax = sns.heatmap(df.corr(), annot=True, cmap='Blues')