import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# Ruta del archivo Excel
file_path = 'C:/Users/aldha/Documents/Datos_SI_Ordenado.xlsx'  # Asegúrate de que la ruta esté correctamente escrita('C:/Users/aldha/Documents/Datos_SI_Ordenado.xlsx')=>Realizar el cambio respectivo

# Verificar si el archivo existe
if not os.path.isfile(file_path):
    raise FileNotFoundError(f"El archivo {file_path} no se encuentra en la ruta especificada.")

# Leer datos desde el archivo Excel
df = pd.read_excel(file_path)

# Seleccionar las columnas a normalizar
columns_to_normalize = [
    'MONTO_PIA', 'MONTO_PIM', 'MONTO_CERTIFICADO', 'MONTO_COMPROMETIDO_ANUAL',
    'MONTO_COMPROMETIDO', 'MONTO_DEVENGADO', 'MONTO_GIRADO'
]

# Comprobar que las columnas existen en el DataFrame
missing_columns = [col for col in columns_to_normalize if col not in df.columns]
if missing_columns:
    raise ValueError(f"Las siguientes columnas no se encontraron en el archivo: {missing_columns}")
#eliminamos las columnas restantes no deseadas
df = df[columns_to_normalize]

# Inicializar el escalador MinMaxScaler
scaler = MinMaxScaler()

# Aplicar el escalador a las columnas seleccionadas
df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

# Guardar los datos normalizados en un nuevo archivo Excel
output_path = 'C:/Users/aldha/Documents/Datos_SI_Normalizado.xlsx'  # Asegúrate de que la ruta de salida esté correctamente escrita
df.to_excel(output_path, index=False)

print(f"Datos normalizados y guardados en '{output_path}'")
