import cv2
import os
import numpy as np

#Aquí se calcula el volumen mínimo, máximo, promedio e individual de cada una de las imágenes en la carpeta

# Obtener la ruta del dir actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Directorio donde se encuentran las imágenes
images_dir = os.path.join(script_dir, 'Propano')

# Crear una lista para almacenar imágenes
processed_images = []

# Iterar sobre las imágenes del directorio, se itera sobre las primeras veinte imágenes porque parecen similares

for i in range(1, 21):  # Iterar del 1 al 20
    # Construir el nombre de la imagen
    image_name = f'image({i}).bmp'
    
    # Construir la ruta relativa de la imagen utilizando images_dir
    image_path = os.path.join(images_dir, image_name)

    # Verificar si existe imagen
    if os.path.isfile(image_path):
        # Cargar la imagen
        image = cv2.imread(image_path)

        # Aplicar el filtro de media con un tamaño de kernel (5x5)
        filtered_image = cv2.blur(image, (5, 5))  

        # Agregar la imagen procesada a la lista
        processed_images.append(filtered_image)
        print(f"Imagen {image_name} procesada.")
    else:
        print(f"La imagen {image_name} no se encontró en la ruta especificada.")

# Verificar la lista de imágenes procesadas
print("Imágenes procesadas:", len(processed_images))

# Calcular la imagen de referencia promediando las imágenes procesadas
if processed_images:
    # Convertir la lista de imágenes procesadas a un array NumPy
    images_array = np.array(processed_images)

    # Calcular el promedio a lo largo del eje 0 (promedio de píxeles)
    reference_image = np.mean(images_array, axis=0).astype(np.uint8)

        # Guardar la imagen de referencia
    reference_image_path = os.path.join(script_dir, 'Propano', 'imagen_referencia.jpg')
    cv2.imwrite(reference_image_path, reference_image)
    print(f"Imagen de referencia guardada en {reference_image_path}")
    
    
    
    
    # Mostrar la imagen de referencia
    cv2.imshow('Imagen de Referencia', reference_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se encontraron imágenes para procesar.")



# Función para calcular el volumen de gas utilizando una regla de tres
def calcular_volumen_gas(area_diff, referencia, porcentaje_referencia):
    volumen_gas = (area_diff * referencia) / porcentaje_referencia
    return volumen_gas


# Función para calcular las diferencias y superponer los resultados en una imagen
def calcular_diferencias(img_referencia, img_folder, img_comparar, umbral):
    # Obtener la ruta del directorio actual donde se encuentra el script Python
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Crear una carpeta para las imágenes de diferencias si no existe
    diff_folder = os.path.join(script_dir, 'Diferencias')
    if not os.path.exists(diff_folder):
        os.makedirs(diff_folder)

    # Leer la imagen de referencia y convertirla a escala de grises
    reference_image_gray = cv2.imread(img_referencia, cv2.IMREAD_GRAYSCALE)

    # Construir las rutas relativas a las imágenes
    img_comparar_path = os.path.join(script_dir, img_comparar)

    # Comparar la imagen de referencia con todas las imágenes de la carpeta
    for filename in os.listdir(img_folder):
        if filename.endswith('.bmp'):
            img_path = os.path.join(img_folder, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Verificar y redimensionar las imágenes si es necesario
            if reference_image_gray.shape != img.shape:
                img = cv2.resize(img, (reference_image_gray.shape[1], reference_image_gray.shape[0]))

            # Calcular la diferencia absoluta entre la imagen de referencia y la imagen actual
            diff_ref = cv2.absdiff(reference_image_gray, img)
            diff_count_ref = np.count_nonzero(diff_ref >= umbral)

            # Calcular el porcentaje de diferencia en relación con el tamaño de la imagen
            area_diff_ref = diff_count_ref / (img.shape[0] * img.shape[1]) * 100

            # Leer la imagen a comparar y convertirla a escala de grises
            img_compare = cv2.imread(img_comparar_path, cv2.IMREAD_GRAYSCALE)
            if img_compare.shape != img.shape:
                img_compare = cv2.resize(img_compare, (img.shape[1], img.shape[0]))

            # Calcular la diferencia absoluta con la imagen a comparar
            diff_compare = cv2.absdiff(img_compare, img)
            diff_count_compare = np.count_nonzero(diff_compare >= umbral)
            area_diff_compare = diff_count_compare / (img.shape[0] * img.shape[1]) * 100

            # Superponer los resultados en la imagen de diferencia
            result_image = cv2.cvtColor(diff_ref, cv2.COLOR_GRAY2BGR)  # Convertir a imagen BGR para superponer texto
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.5
            font_thickness = 1
            font_color = (0, 255, 0)  # Color verde para el texto

            # Texto para superponer en la imagen
            text = f'Dif. Ref {area_diff_ref:.2f}%, Dif. Comp: {area_diff_compare:.2f}%'

            # Superponer texto en la imagen (debajo de la imagen)
            cv2.putText(result_image, text, (10, result_image.shape[0] - 20), font, font_scale, font_color, font_thickness)

            # Ajustar el contraste de la imagen resultante
            alpha = 3.5  # Factor de contraste
            beta = 2  # Factor de brillo
            result_image_contrast = cv2.convertScaleAbs(result_image, alpha=alpha, beta=beta)

            # Guardar la imagen resultante en la carpeta de diferencias con mayor contraste
            result_path = os.path.join(diff_folder, filename)
            cv2.imwrite(result_path, result_image_contrast)

    print('Imágenes de diferencias generadas correctamente en la carpeta "Diferencias".')

    # Crear o abrir el archivo de texto para escribir los resultados
    results_file_path = os.path.join(diff_folder, 'resultados.txt')

    # Variables para el volumen máximo, mínimo y sumatoria de volúmenes
    volumen_maximo = 0
    volumen_minimo = 0
    sumatoria_volumenes = 0
    num_imagenes = 0
    volumen_total=0







    with open(results_file_path, 'w') as results_file:
        results_file.write('Nombre de Imagen | Dif. con Referencia (%) | Dif. con Comparación (%) | Volumen Gas (litros)\n')
        results_file.write('----------------------------------------------------------------------------------------\n')

        # Comparar la imagen de referencia con todas las imágenes de la carpeta
        for filename in os.listdir(img_folder):
            if filename.endswith('.bmp'):
                img_path = os.path.join(img_folder, filename)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

                # Verificar y redimensionar las imágenes si es necesario
                if reference_image_gray.shape != img.shape:
                    img = cv2.resize(img, (reference_image_gray.shape[1], reference_image_gray.shape[0]))

                # Calcular la diferencia absoluta entre la imagen de referencia y la imagen actual
                diff_ref = cv2.absdiff(reference_image_gray, img)
                diff_count_ref = np.count_nonzero(diff_ref >= umbral)

                # Calcular el porcentaje de diferencia con la referencia
                area_diff_ref = diff_count_ref / (img.shape[0] * img.shape[1]) * 100

                # Leer la imagen a comparar y convertirla a escala de grises
                img_compare = cv2.imread(img_comparar_path, cv2.IMREAD_GRAYSCALE)
                if img_compare.shape != img.shape:
                    img_compare = cv2.resize(img_compare, (img.shape[1], img.shape[0]))

                # Calcular la diferencia absoluta con la imagen a comparar
                diff_compare = cv2.absdiff(img_compare, img)
                diff_count_compare = np.count_nonzero(diff_compare >= umbral)
                area_diff_compare = diff_count_compare / (img.shape[0] * img.shape[1]) * 100

                # Calcular el volumen de gas de forma proporcional
                volumen_gas = calcular_volumen_gas(area_diff_ref, referencia=5, porcentaje_referencia=13)
                

                # Actualizar volumen máximo, mínimo y sumatoria de volúmenes

                if volumen_gas > volumen_maximo:
                    volumen_maximo = volumen_gas
                    

                if volumen_gas < volumen_minimo:
                    volumen_minimo = volumen_gas
                    

                sumatoria_volumenes += volumen_gas
                num_imagenes += 1

                # Escribir los resultados en el archivo de texto
                results_file.write(f'{filename} | {area_diff_ref:.2f}% | {area_diff_compare:.2f}% | {volumen_gas:.2f}\n')

                volumen_total=volumen_total+volumen_gas


    # Después del bucle de procesamiento de imágenes
    # Calcular el volumen promedio



        
    
    # Agregar la información de volumen máximo, mínimo y promedio al archivo de resultados
    with open(results_file_path, 'a') as results_file:
        # Calcular el volumen promedio
        try:
            volumen_promedio = volumen_total / num_imagenes
        except:
            print('0')

        
        # Mostrar los resultados de volumen máximo, mínimo y promedio
        print(f'Volumen máximo: {volumen_maximo:.2f} litros')
        print(f'Volumen mínimo: {volumen_minimo:.2f} litros')
        print(f'Volumen promedio: {volumen_promedio:.2f} litros')

        # Agregar la información de volumen máximo, mínimo y promedio al archivo de resultados
        results_file.write(f'Volumen Máximo: {volumen_maximo:.2f} litros\n')
        results_file.write(f'Volumen Mínimo: {volumen_minimo:.2f} litros\n')
        results_file.write(f'Volumen Promedio: {volumen_promedio:.2f} litros\n')



    return volumen_promedio, volumen_maximo, volumen_minimo, volumen_gas, num_imagenes, volumen_total


# Directorio donde se encuentran las imágenes de la carpeta y la imagen a comparar
img_folder = 'Punto_1/Propano'
img_comparar = 'Propano/propano5L.jpg'

# Ruta relativa de la imagen de referencia
img_referencia = os.path.join(img_folder, 'imagen_referencia.jpg')

# Verificar si la imagen de referencia se encuentra en la ruta especificada
if os.path.exists(img_referencia):
    print("La imagen de referencia se encontró en la ruta especificada.")
    # Continuar con el procesamiento de las imágenes...
    calcular_diferencias(img_referencia, img_folder, img_comparar, umbral=5)
else:
    print("Error: La imagen de referencia no se encontró en la ruta especificada.")






    






