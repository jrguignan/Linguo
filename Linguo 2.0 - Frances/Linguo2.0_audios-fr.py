import os
import pandas as pd
import re
from gtts import gTTS

# Mensaje al usuario
print("El programa puede tardar un par de minutos, depende del tamaño del archivo vocabulario\n")

# Nombre del archivo CSV
csv_file = "vocabulario.csv"

# Crear la carpeta de audio si no existe
audio_folder = "audio"
os.makedirs(audio_folder, exist_ok=True)

# Cargar el archivo CSV asegurando compatibilidad con caracteres especiales
df = pd.read_csv(csv_file, encoding="utf-8")

# Capitalizar todas las palabras en todas las filas y columnas
df.columns = [col.title() for col in df.columns]
df = df.applymap(lambda x: str(x).strip().title() if isinstance(x, str) else x)
df.to_csv(csv_file, index=False, encoding="utf-8")

# Función para limpiar y formatear el nombre del archivo con caracteres franceses
def limpiar_nombre(archivo):
    archivo_limpio = re.sub(r'[^a-zA-ZÀ-ÿ0-9 ]', ' ', archivo).strip()  # Permitir caracteres franceses
    return archivo_limpio.replace(" ", "_").replace("...", "").replace("-", "_").replace("'", "_").replace("?", "")

# Iterar sobre cada palabra en la primera columna y generar el audio
for palabra in df.iloc[:, 0]:  # Tomar solo la primera columna
    if isinstance(palabra, str) and palabra.strip():
        nombre_limpio = limpiar_nombre(palabra)  # Limpiar el nombre del archivo
        audio_path = os.path.join(audio_folder, f"{nombre_limpio}.mp3")
        
        try:
            tts = gTTS(text=palabra, lang="fr")  # Generar audio en francés
            tts.save(audio_path)
            print(f"Audio guardado: {audio_path}")
        except Exception as e:
            print(f"Error al generar audio para '{palabra}': {e}")

print("\n¡Proceso completado!\n")
print("Ya se guardaron los audios, puede cerrar esta ventana")
