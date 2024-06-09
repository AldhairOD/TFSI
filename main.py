#Cargado de datos
import csv
import chardet
import pandas as pd
import numpy as np
import io
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.base import TransformerMixin
from sklearn.preprocessing import RobustScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

archivo = "C:/Users/aldha/Documents/Datos_SI_Normalizado.xlsx" #Realizar el cambio según su PC

# Leer solo algunas columnas de un archivo Excel
columnas_a_leer = ['MONTO_PIA', 'MONTO_PIM', 'MONTO_CERTIFICADO', 'MONTO_COMPROMETIDO_ANUAL', 'MONTO_COMPROMETIDO', 'MONTO_DEVENGADO', 'MONTO_GIRADO']
df = pd.read_excel(archivo, usecols=columnas_a_leer)

#Mostramos algunos datos
df.head(14000)
#Mostramos los últimos datos
df.tail()
#Revisamos la información del archivo .csv
df.info()
