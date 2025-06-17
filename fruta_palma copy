import cv2
import numpy as np
import os

# Ruta a la carpeta de entrada con imágenes BMP
input_folder = "C:/Users/jdoso/Documents/Nestle/Archivo"


# Crear una carpeta para guardar las imágenes procesadas
output_folder = os.path.join(input_folder, "resaltados_grises")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Procesar cada imagen en la carpeta
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        # Leer la imagen original
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Suavizar la imagen (opcional, para reducir ruido)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)

        # Convertir a escala de grises
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

        # Detectar bordes con el algoritmo Canny
        edges = cv2.Canny(gray, 50, 150)  # Ajusta los umbrales (50 y 150) según la intensidad deseada

        # Combinar los bordes con la imagen original en escala de grises
        combined = cv2.addWeighted(gray, 0.7, edges, 0.3, 0)

        # Guardar la imagen resultante
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, combined)

        print(f"Imagen procesada y guardada: {output_path}")

print(f"Todas las imágenes han sido procesadas y guardadas en: {output_folder}")