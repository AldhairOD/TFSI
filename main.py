#Cargado de datos
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import CurvaCodo as cc

archivo = "C:/Users/aldha/Documents/Datos_SI_Normalizado.xlsx" #Realizar el cambio según su PC

# Leer solo algunas columnas de un archivo Excel
columnas_a_leer = ['MONTO_PIA', 'MONTO_PIM', 'MONTO_CERTIFICADO', 'MONTO_COMPROMETIDO_ANUAL', 'MONTO_COMPROMETIDO', 'MONTO_DEVENGADO', 'MONTO_GIRADO']
df = pd.read_excel(archivo, usecols=columnas_a_leer)


#Eliminamos las columnas con valores Nan en el .csv
df = df.dropna()

cc.curva(archivo, columnas_a_leer, df)