import cv2
import numpy as np
import os


# Genera carpetas de recortes donde se enfoca el primer plano la galleta 
#Genera una carpeta de imágenes concatenadas de la imagen original, el recorte suavizado y el recorte original

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Carpeta que contiene las imágenes a evaluar
folder_path = os.path.join(current_dir, 'Galletas/Bueno')

# Carpeta donde se guardarán las imágenes concatenadas
output_folder = os.path.join(folder_path, 'Recortes')

# Carpeta donde se guardarán las imágenes concatenadas
concat_folder = os.path.join(folder_path, 'concat')

# Carpeta que contiene las imágenes a evaluar
folder_path2 = os.path.join(current_dir, 'Galletas/Incorrecto')

# Carpeta donde se guardarán las imágenes concatenadas
output_folder2 = os.path.join(folder_path2, 'Recortes')

# Carpeta donde se guardarán las imágenes concatenadas
concat_folder2 = os.path.join(folder_path2, 'concat')



# Verificar si la carpeta de salida existe, y si no, crearla
if not os.path.exists(output_folder):
    os.makedirs(concat_folder)
    os.makedirs(output_folder)



# Verificar si la carpeta de salida existe, y si no, crearla
if not os.path.exists(output_folder2):

    os.makedirs(concat_folder2)
    os.makedirs(output_folder2)

# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)

# Obtener la lista de archivos en la carpeta
file_list2 = os.listdir(folder_path2)
print(file_list2)

# Iterar a través de cada imagen en la carpeta
for file_name in file_list:
    try:
        # Obtener la ruta completa de la imagen
        image_path = os.path.join(folder_path, file_name)

        # Cargar la imagen
        image = cv2.imread(image_path)

        # Verificar que la imagen se haya cargado correctamente
        if image is not None:
            # Convertir la imagen a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Aplicar un suavizado para reducir el ruido y mejorar la detección de bordes
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 5)

            # Aplicar el detector de círculos de Hough con parámetros ajustados
            circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1.7, minDist=600, param1=260, param2=30,
                                       minRadius=130, maxRadius=200)
            

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    # Verificar si el centro del círculo está dentro de un rango específico en la imagen
                    if x - r > 0 and y - r > 0 and x + r < image.shape[1] and y + r < image.shape[0]:
                        # Dibujar el círculo y su borde en la imagen original
                        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

                        # Crear una máscara del círculo detectado
                        mask = np.zeros_like(gray_image)
                        cv2.circle(mask, (x, y), r, (255, 255, 255), -1)  # Rellenar el círculo con blanco en la máscara

                        # Aplicar la máscara a la imagen original para obtener solo el interior del círculo
                        masked_image = cv2.bitwise_and(image, image, mask=mask)

                        # Aplicar un suavizado leve al interior del círculo
                        smoothed_masked_image = cv2.GaussianBlur(masked_image, (3, 3), 1)

                        # Recortar la región original correspondiente al círculo
                        x1, y1 = max(0, x - r), max(0, y - r)
                        x2, y2 = min(image.shape[1], x + r), min(image.shape[0], y + r)
                        cropped_original = image[y1:y2, x1:x2]

                        # Guardar el recorte original
                        output_path = os.path.join(output_folder, f'cropped_original_{file_name}')
                        cv2.imwrite(output_path, cropped_original)

                # Concatenar las tres imágenes
                concatenated_image = cv2.hconcat([image, smoothed_masked_image, masked_image])

                # Agregar texto al resultado
                text = "Original completa,                                                                   Recorte suavizado,                                                                                     Recorte original"
                cv2.putText(concatenated_image, text, (10, concatenated_image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 1, cv2.LINE_AA)

                # Guardar la imagen concatenada en la carpeta "concat"
                output_path = os.path.join(concat_folder, f'concat_{file_name}')
                cv2.imwrite(output_path, concatenated_image)





    except Exception as e:
        print(f"Error al procesar la imagen, la galleta no está en el lugar predeterminado {file_name}: {str(e)}")
        continue

print('Bueno, listo')




# Iterar a través de cada imagen en la carpeta
for file_name2 in file_list2:
    try:
        # Obtener la ruta completa de la imagen
        image_path = os.path.join(folder_path2, file_name2)

        # Cargar la imagen
        image = cv2.imread(image_path)

        # Verificar que la imagen se haya cargado correctamente
        if image is not None:
            # Convertir la imagen a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Aplicar un suavizado para reducir el ruido y mejorar la detección de bordes
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 5)

            # Aplicar el detector de círculos de Hough con parámetros ajustados
            circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1.7, minDist=600, param1=260, param2=30,
                                       minRadius=130, maxRadius=200)
            

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    # Verificar si el centro del círculo está dentro de un rango específico en la imagen
                    if x - r > 0 and y - r > 0 and x + r < image.shape[1] and y + r < image.shape[0]:
                        # Dibujar el círculo y su borde en la imagen original
                        cv2.circle(image, (x, y), r, (0, 255, 0), 2)

                        # Crear una máscara del círculo detectado
                        mask = np.zeros_like(gray_image)
                        cv2.circle(mask, (x, y), r, (255, 255, 255), -1)  # Rellenar el círculo con blanco en la máscara

                        # Aplicar la máscara a la imagen original para obtener solo el interior del círculo
                        masked_image = cv2.bitwise_and(image, image, mask=mask)

                        # Aplicar un suavizado leve al interior del círculo
                        smoothed_masked_image = cv2.GaussianBlur(masked_image, (3, 3), 1)

                        # Recortar la región original correspondiente al círculo
                        x1, y1 = max(0, x - r), max(0, y - r)
                        x2, y2 = min(image.shape[1], x + r), min(image.shape[0], y + r)
                        cropped_original = image[y1:y2, x1:x2]

                        # Guardar el recorte original
                        output_path = os.path.join(output_folder2, f'cropped_original_{file_name2}')
                        cv2.imwrite(output_path, cropped_original)

                # Concatenar las tres imágenes
                concatenated_image = cv2.hconcat([image, smoothed_masked_image, masked_image])

                # Agregar texto al resultado
                text = "Original completa,                                                                   Recorte suavizado,                                                                                     Recorte original"
                cv2.putText(concatenated_image, text, (10, concatenated_image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 255, 255), 1, cv2.LINE_AA)

                # Guardar la imagen concatenada en la carpeta "concat"
                output_path = os.path.join(concat_folder2, f'concat_{file_name2}')
                cv2.imwrite(output_path, concatenated_image)





    except Exception as e:
        print(f"Error al procesar la imagen, la galleta no está en el lugar predeterminado {file_name2}: {str(e)}")
        continue

print('Incorrecto, listo')



