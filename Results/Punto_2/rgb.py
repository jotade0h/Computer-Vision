import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Obtener la ruta del directorio actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa de la imagen
image_path = os.path.join(script_dir, 'Galletas/Bueno/Recortes/cropped_original_Imagen00000.bmp')

# Verificar si la imagen existe en la ruta especificada
if os.path.isfile(image_path):
    # Cargar la imagen en color (BGR)
    original_image = cv2.imread(image_path)

    # Convertir la imagen a escala de grises
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Encontrar contornos en la imagen
    contours, _ = cv2.findContours(gray_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en la imagen original
    contoured_image = cv2.drawContours(original_image.copy(), contours, -1, (0, 255, 0), 2)

    # Separar los canales de color
    b, g, r = cv2.split(original_image)

    # Mostrar la imagen original, sus componentes RGB, escala de grises, escala de grises invertida y contornos
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    # Mostrar la imagen original
    axes[0, 0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title('Imagen Original')
    axes[0, 0].axis('off')

    # Mostrar el componente Rojo (R)
    axes[0, 1].imshow(r, cmap='Reds')
    axes[0, 1].set_title('Componente Rojo (R)')
    axes[0, 1].axis('off')

    # Mostrar el componente Verde (G)
    axes[0, 2].imshow(g, cmap='Greens')
    axes[0, 2].set_title('Componente Verde (G)')
    axes[0, 2].axis('off')

    # Mostrar la imagen en escala de grises
    axes[1, 0].imshow(b, cmap='Blues')
    axes[1, 0].set_title('Escala de Grises')
    axes[1, 0].axis('off')

    # Mostrar la imagen en escala de grises invertida
    axes[1, 1].imshow(255 - gray_image, cmap='gray')
    axes[1, 1].set_title('Escala de Grises Invertida')
    axes[1, 1].axis('off')

    # Mostrar los contornos en la imagen original
    axes[1, 2].imshow(cv2.cvtColor(contoured_image, cv2.COLOR_BGR2RGB))
    axes[1, 2].set_title('Contornos')
    axes[1, 2].axis('off')

    # Ajustar el espaciado entre subplots
    plt.tight_layout(pad=1.0)

    # Mostrar las imágenes
    plt.show()
else:
    print("La imagen no se encontró en la ruta especificada")
