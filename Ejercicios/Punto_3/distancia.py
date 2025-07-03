import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Obtener la ruta del directorio actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa de la imagen
image_path = os.path.join(script_dir, 'Punto_3.jpeg')

# Cargar la imagen
image = cv2.imread(image_path)



# Aplicar suavizado para reducir el ruido
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Aplicar el operador Sobel
sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)

# Calcular la magnitud y la orientación de los gradientes
magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
orientation = np.arctan2(sobel_y, sobel_x)

# Aplicar el algoritmo de detección de bordes Canny
edges = cv2.Canny(blurred, 50, 150)










ancho, alto, _=image.shape
print(ancho,alto)

P1x,P1y=(int(602/.75),int(551/.75))
P2x,P2y=(int(1178/.75),int(597/.75))
P3x,P3y=(int(759/.75),int(562/.75))
P4x,P4y=(int(866/.75),int(570/.75))
P5x,P5y=(int(655/.75),int(608/.75))
P6x,P6y=(int(792/.75),int(622/.75))


# Definir las coordenadas de los 6 puntos
points = [(P1x, P1y), (P2x,P2y), (P3x,P3y), (P4x,P4y), (P5x,P5y), (P6x,P6y)]

# Dibujar los puntos en la imagen
for point in points:
    cv2.circle(image, point, radius=5, color=(0, 255, 0), thickness=-1)  # Dibujar círculos rellenos en verde

# Conectar algunos puntos con líneas
cv2.line(image, points[0], points[1], color=(0, 0, 255), thickness=2)
cv2.line(image, points[2], points[3], color=(0, 255, 255), thickness=2)
cv2.line(image, points[4], points[5], color=(255, 0, 255), thickness=2)


sobelfigure=np.abs(sobel_x)

# Conectar algunos puntos con líneas
cv2.line(sobelfigure, points[0], points[1], color=(0, 0, 255), thickness=2)
cv2.line(sobelfigure, points[2], points[3], color=(0, 255, 255), thickness=2)
cv2.line(sobelfigure, points[4], points[5], color=(255, 0, 255), thickness=2)



fig = plt.figure(figsize=(15, 10))  # Tamaño de la figura (10 pulgadas de ancho y 5 pulgadas de alto)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobelfigure, cmap='gray')
plt.title('Sobel X')
plt.axis('off')

# Agregar los puntos a la imagen original
for point in points:
    plt.plot(point[0], point[1], 'ro')  # 'ro' indica puntos rojos

plt.show()

print((P1x,P1y), 'Punto 1 \n',(P2x,P2y),'Punto 2 \n',(P3x,P3y),'Punto 3 \n',(P4x,P4y),'Punto 4 \n',(P5x,P5y),'Punto 5 \n',(P6x,P6y), 'Punto 6 \n')









#ecn1=> lc+delta=770p (Punto 2-1)
#ecn2=> lp+delta=143p (Punto 4-3)
#ecn3=> mov_llanta+delta=184p (Punto 6-5)

#Suponiendo el movimiento de la llanta 113cm (llanta+delta)
#Llanta de aproximadamente 75cm, da un delta de 38cm
#lc=400cm
#velocidad=13.75km/h

