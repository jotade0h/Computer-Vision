import glob
import os
import rasterio

def verificar_banda(path_safe, banda):
    patron = os.path.join(path_safe, "GRANULE", "*", "IMG_DATA", "R10m", f"*_{banda}_10m.jp2")
    archivos = glob.glob(patron)
    if not archivos:
        print(f"❌ No se encontró la banda {banda} en {path_safe}")
        return None
    print(f"✅ Banda {banda} encontrada: {archivos[0]}")
    return archivos[0]

# Rutas a tus carpetas .SAFE
ruta_2017 = "data/S2A_MSIL2A_20170124T101311_N0500_R022_T32TQR_20231026T122958.SAFE"
ruta_2025 = "data/S2B_MSIL2A_20250127T101209_N0511_R022_T32TQR_20250127T130241.SAFE"

print("\n📦 Verificando archivos para 2017...")
verificar_banda(ruta_2017, "B04")
verificar_banda(ruta_2017, "B08")

print("\n📦 Verificando archivos para 2025...")
verificar_banda(ruta_2025, "B04")
verificar_banda(ruta_2025, "B08")
