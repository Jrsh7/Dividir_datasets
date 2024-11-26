import os
import shutil
import random

# Configuración
ruta_carpeta = r"C:\Users\jrshm\Desktop\Entrenamiento IA\dataset\dog"

# Obtener ruta del escritorio del usuario
ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")

# Crear rutas de destino en el escritorio
ruta_destino_1 = os.path.join(ruta_escritorio, "dataset_1")
ruta_destino_2 = os.path.join(ruta_escritorio, "dataset_2")

proporcion = 0.5  # Proporción para dividir (50% en cada carpeta)

# Crear carpetas de destino si no existen
os.makedirs(ruta_destino_1, exist_ok=True)
os.makedirs(ruta_destino_2, exist_ok=True)

# Obtener lista de imágenes
imagenes = [img for img in os.listdir(ruta_carpeta) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Mezclar imágenes de manera aleatoria
random.shuffle(imagenes)

# Calcular cuántas imágenes irán a cada carpeta
limite = int(len(imagenes) * proporcion)

# Dividir las imágenes
imagenes_1 = imagenes[:limite]
imagenes_2 = imagenes[limite:]

# Mover imágenes a la primera carpeta
for img in imagenes_1:
    shutil.move(os.path.join(ruta_carpeta, img), os.path.join(ruta_destino_1, img))

# Mover imágenes a la segunda carpeta
for img in imagenes_2:
    shutil.move(os.path.join(ruta_carpeta, img), os.path.join(ruta_destino_2, img))

print("¡Las imágenes se han dividido correctamente en el escritorio!")
