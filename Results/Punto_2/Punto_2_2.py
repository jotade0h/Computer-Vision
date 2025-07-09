import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Este script calcula el número de imágenes incorrectas en cada carpeta, por lo que se debe compilar dos veces, 
# en pantalla muestar los resultados por imagen, sin embargo, también genera un archivo txt con los resultados
# comentando la segunda ocasión la linea mencionada más abajo. Comentarla permite que se trabaje sobre la carpeta 
# de galletas en buen estado

# Ruta relativa de la carpeta de imágenes
img_folder = 'Galletas/Bueno/Recortes/'



# Ruta relativa de la carpeta de imágenes

############### SI DESEA MIRAR EL RENDIMIENTO PAR LAS GALLETAS INCORRECTAS, NO COMENTAR LA SIGUIENTE LINEA
#img_folder = 'Galletas/Incorrecto/Recortes/'
###############


# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Carpeta que contiene las imágenes
folder_path = os.path.join(current_dir, img_folder)


# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)

print(folder_path)


# Inicializar variables para el valor máximo del promedio de la imagen inversa
max_promedio_inversa = 0
# Inicializar variables para el número de píxeles blancos, porcentaje máximo y mínimo
max_pixeles_blancos = 0
min_pixeles_blancos = float('inf')
max_porcentaje_blancos = 0
min_porcentaje_blancos = 100

if img_folder == 'Galletas/Bueno/Recortes/':
    result_file = os.path.join(current_dir, 'Galletas/Bueno/resultados.txt')
else:
    result_file = os.path.join(current_dir, 'Galletas/Incorrecto/resultados.txt')




# Recorrer todas las imágenes en la carpeta Bueno


# Abrir el archivo de resultados para escritura
with open(result_file, 'w') as f:
    cont=0
    f.write("Nombre de archivo | Correcto/Incorrecto | Pixeles diferentes de cero | Promedio de intensidad | Máximo | Mínimo | Pixeles blancos generados por el relleno | Pixeles dentro del círculo | Porcentaje de blancos/pixeles del círculo\n")

    for filename in file_list:
        print(filename)
        if filename.endswith('.BMP'):
            
            img_path = os.path.join(folder_path, filename)
            
            img = cv2.imread(img_path)

            # Convertir la imagen a escala de grises
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Obtener las dimensiones de la imagen
            alto, ancho = gray.shape[:2]
            
            
            

            # Definir el punto de inicio para el relleno
            seed_point = (int(ancho*2/3)+20, int(alto*2/3)-40)  # Coordenadas del punto de inicio
            




            
            
            # Aplicar filtro gaussiano para suavizar la imagen y potenciar textura
            img = cv2.GaussianBlur(img, (0, 0), sigmaX=2, sigmaY=2)
                    
            # Realizar el relleno
            cv2.floodFill(img, mask=None, seedPoint=seed_point, newVal=(255, 255, 255), loDiff=(50, 50, 25), upDiff=(60,60, 150), flags=cv2.FLOODFILL_FIXED_RANGE)



            # Convertir la imagen a escala de grises para tener de referencia
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            radio = int(alto/2)
            area_circ=np.pi*radio**2


            # Crear una máscara circular para el área del círculo
            mascara = np.zeros((alto, ancho), dtype=np.uint8)
            cv2.circle(mascara, (ancho // 2, alto // 2), radio, 255, -1)  # Dibujar el círculo en la máscara

            # Aplicar la máscara al relleno para contar solo los píxeles blancos dentro del círculo
            relleno_en_circulo = cv2.bitwise_and(gray, gray, mask=mascara)
            pixeles_blancos_relleno = np.sum(relleno_en_circulo == 255)

            


            # Definir el centro y el radio del círculo
            centro = (alto, ancho)  # Coordenadas del centro del círculo (x, y)
            radio = int(alto/2)  # Radio del círculo

            # Crear una máscara circular del mismo tamaño que la imagen
            mask = np.zeros_like(gray)
            cv2.circle(mask, centro, radio, 255, -1)


            # Aplicar la máscara a la imagen para obtener los píxeles dentro del círculo
            pixels_circulo1 = cv2.bitwise_and(gray, mask)

            # Obtener los valores de intensidad de los píxeles diferentes de cero dentro del círculo
            valores_diferentes_de_cero = pixels_circulo1[pixels_circulo1 != 0]

            # Calcular la cantidad de píxeles diferentes de cero y su promedio de intensidad
            cantidad_diferentes_de_cero = len(valores_diferentes_de_cero)

            # Calcular máximo, mínimo, promedio
            maximo = np.max(valores_diferentes_de_cero)
            minimo = np.min(valores_diferentes_de_cero)
            promedio_intensidad = np.mean(valores_diferentes_de_cero)

            print(f"Píxeles diferentes de cero: {cantidad_diferentes_de_cero}")
            print(f"Promedio de intensidad: {promedio_intensidad:.2f}")
            print(f"Máximo: {maximo}")
            print(f"Mínimo: {minimo}")



            
            # Contar píxeles dentro del círculo
            pixeles_totales = np.sum(mascara == 255)

            # Calcular el número de píxeles dentro del círculo
            pixeles_circulo = np.sum(mascara == 255)

            print('Número de píxeles blancos generados por el relleno:', pixeles_blancos_relleno)
            print('Número de píxeles dentro del círculo de radio ancho/2:', pixeles_circulo)
            print(f"Promedio de intensidad: {promedio_intensidad}")
            print(f"Porcentaje de blancos/ pixeles del circulo: {pixeles_blancos_relleno/pixeles_circulo*100:.2f}%")

            if pixeles_blancos_relleno/pixeles_circulo > 0.242 or promedio_intensidad <120:
            

                if pixeles_blancos_relleno/pixeles_circulo < 0.545:
                    cv2.putText(gray, 'Correcto', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                    resultado='Correcto'
                else:
                    cv2.putText(gray, 'Incorrecto', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                    cont+=1
                    resultado='Incorrecto'
            elif pixeles_blancos_relleno/pixeles_circulo < 0.242 and promedio_intensidad > 110:

                cv2.putText(gray, 'Incorrecto', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                resultado='Incorrecto'

            # Escribir datos en el archivo de resultados
            f.write("{:s} | {:s} | {:d} | {:.2f} | {:.2f} | {:.2f} | {:d} | {:d} | {:.2f}%\n".format(filename, resultado, cantidad_diferentes_de_cero, promedio_intensidad, maximo, minimo,
            pixeles_blancos_relleno, pixeles_circulo, pixeles_blancos_relleno / pixeles_circulo * 100))


            
            # Mostrar la imagen
            """cv2.imshow('Imagen', gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()"""

    if img_folder == 'Galletas/Bueno/Recortes/':
        print(cont, ' Galletas incorrectas, ', f'Porcentaje de aciertos: {((1-cont/len(file_list)))*100:.2f}%' )
        f.write(f'Porcentaje de aciertos: {((1-cont/len(file_list)))*100:.2f}%')
    else:
        print(cont, ' Galletas incorrectas, ', f'Porcentaje de aciertos: {((cont/len(file_list)))*100:.2f}%' )
        f.write(f'Porcentaje de aciertos: {((cont/len(file_list)))*100:.2f}%')












