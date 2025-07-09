import os
import glob

def listar_bandas_en_safe(path_safe):
    print(f"\n🔎 Explorando: {path_safe}")



    # 🧪 DEBUG: listar carpetas dentro de GRANULE
    granule_path = os.path.join(path_safe, "GRANULE")
    print(f"📂 Contenido de {granule_path}:")
    if os.path.exists(granule_path):
        print("📁 Subcarpetas:", os.listdir(granule_path))
    else:
        print("🚫 No existe la carpeta GRANULE")

    # 🧪 DEBUG: buscar manualmente archivos .jp2 en todo el .SAFE
    print("🔍 Buscando manualmente archivos .jp2 en todo el árbol de carpetas...")
    for root, dirs, files in os.walk(path_safe):
        for file in files:
            if file.endswith(".jp2"):
                print("✅ Encontrado:", os.path.join(root, file))


                
    # Buscar todos los archivos .jp2 dentro de IMG_DATA (en cualquier resolución)
    ruta = os.path.join(path_safe, "GRANULE", "*", "IMG_DATA", "*","*.jp2")
    archivos = glob.glob(ruta)

    if not archivos:
        print("🚫 No se encontraron archivos .jp2 en esta carpeta.")
        return

    # Extraer nombres de bandas
    bandas_encontradas = {}
    for archivo in archivos:
        nombre = os.path.basename(archivo)
        if "_B" in nombre:
            partes = nombre.split("_")
            for parte in partes:
                if parte.startswith("B") and parte[1:].isdigit():
                    banda = parte
                    resolucion = nombre.split("_")[-1].replace(".jp2", "")
                    bandas_encontradas[banda] = resolucion

    if bandas_encontradas:
        print("📊 Bandas encontradas:")
        for banda, res in sorted(bandas_encontradas.items()):
            print(f"  - {banda}: {res}")
    else:
        print("⚠️ No se pudieron identificar las bandas de forma automática.")

# 🧪 Cambia aquí tus carpetas .SAFE a revisar
carpetas_safe = [
    "data/S2A_MSIL2A_20170124T101311_N0500_R022_T32TQR_20231026T122958.SAFE",
    "data/S2B_MSIL2A_20250127T101209_N0511_R022_T32TQR_20250127T130241.SAFE"
]

for carpeta in carpetas_safe:
    if os.path.exists(carpeta):
        listar_bandas_en_safe(carpeta)
    else:
        print(f"🚫 No existe la carpeta: {carpeta}")
