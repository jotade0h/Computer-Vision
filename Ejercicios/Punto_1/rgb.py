import cv2
import numpy as np
import matplotlib.pyplot as plt
import os



"""Este código genera imágenes RGB, escala de grises, 
imagen inversa para tener diversos puntos de visualización del primer problema, en este caso de la imagen 40"""





# Obtener la ruta del directorio actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa de la imagen
image_path = os.path.join(script_dir, 'Propano/image(40).bmp')

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

    # Mostrar la imagen original, sus componentes RGB y escala de grises
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

    # Mostrar el componente Azul (B)
    axes[1, 0].imshow(b, cmap='Blues')
    axes[1, 0].set_title('Componente Azul (B)')
    axes[1, 0].axis('off')

    # Mostrar la imagen en escala de grises
    axes[1, 1].imshow(gray_image, cmap='gray')
    axes[1, 1].set_title('Escala de Grises')
    axes[1, 1].axis('off')


    # Ruta relativa de la imagen
    image_path2 = os.path.join(script_dir, 'Diferencias/image(40).bmp')


    # Cargar la imagen usando OpenCV
    img_gray = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)


    # Mostrar la imagen en escala de grises
    axes[1, 2].imshow(img_gray, cmap='gray')  # Utiliza cmap='gray' para mostrar la imagen en escala de grises
    axes[1, 2].set_title('Imagen negativa')
    axes[1, 2].axis('off')



    # Ajustar el espaciado entre subplots
    plt.tight_layout(pad=1.0)

    # Mostrar las imágenes
    plt.show()
else:
    print("La imagen no se encontró en la ruta especificada")
