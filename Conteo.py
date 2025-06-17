import os

# Función para contar los números en cada archivo dentro de una carpeta
def contar_numeros_en_archivos(carpeta):
    conteos = {}
    # Iterar sobre todos los archivos en la carpeta
    for archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, archivo)
        # Asegurarse de que es un archivo
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r') as f:
                for linea in f:
                    # Leer el primer número de cada línea
                    primer_numero = int(linea.split()[0])
                    # Sumar al contador si ya está en el diccionario, si no, inicializar en 1
                    if primer_numero in conteos:
                        conteos[primer_numero] += 1
                    else:
                        conteos[primer_numero] = 1
    return conteos

# Rutas de las carpetas
carpetas = ['C:/Users/jdoso/Desktop/Yolov8/Fruits3/train/labels', 'C:/Users/jdoso/Desktop/Yolov8/Fruits3/valid/labels', 'C:/Users/jdoso/Desktop/Yolov8/Fruits3/test/labels']

# Contar los números para cada carpeta
conteos_totales = {}
for carpeta in carpetas:
    conteos_carpeta = contar_numeros_en_archivos(carpeta)
    # Sumar los resultados al conteo total
    for num, count in conteos_carpeta.items():
        if num in conteos_totales:
            conteos_totales[num] += count
        else:
            conteos_totales[num] = count

# Mostrar los resultados
print("Conteo total de números:")
for num, count in conteos_totales.items():
    print(f"Número {num}: {count} ocurrencias")
