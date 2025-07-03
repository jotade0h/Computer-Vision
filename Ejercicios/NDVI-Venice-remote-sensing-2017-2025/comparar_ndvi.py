import os
import glob
import numpy as np
import rasterio
import matplotlib.pyplot as plt
from rasterio.enums import Resampling

def buscar_banda(path_safe, banda):
    """Busca el archivo .jp2 correspondiente a la banda deseada dentro de una carpeta .SAFE"""
    ruta_base = os.path.join(path_safe, "GRANULE")
    for granule in os.listdir(ruta_base):
        ruta_img = os.path.join(ruta_base, granule, "IMG_DATA")
        for root, dirs, files in os.walk(ruta_img):
            for file in files:
                if f"_{banda}_" in file and file.endswith(".jp2"):
                    return os.path.join(root, file)
    raise FileNotFoundError(f"No se encontró la banda {banda} en {path_safe}")

def calcular_ndvi(nir_path, red_path):
    """Calcula el NDVI dado el path a las bandas NIR y RED"""
    with rasterio.open(nir_path) as nir_src:
        nir = nir_src.read(1).astype(float)
        profile = nir_src.profile

    with rasterio.open(red_path) as red_src:
        red = red_src.read(1).astype(float)

    ndvi = (nir - red) / (nir + red + 1e-10)
    return ndvi, profile

# === 📁 Definir rutas base ===
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(script_dir)
data_dir = os.path.join(base_dir, "data")
result_dir = os.path.join(data_dir, "results")

# Crear carpeta de resultados si no existe
os.makedirs(result_dir, exist_ok=True)

# Carpetas SAFE
carpeta_2017 = os.path.join(data_dir, "S2A_MSIL2A_20170124T101311_N0500_R022_T32TQR_20231026T122958.SAFE")
carpeta_2025 = os.path.join(data_dir, "S2B_MSIL2A_20250127T101209_N0511_R022_T32TQR_20250127T130241.SAFE")

# === Procesamiento ===
print("📦 Buscando bandas en 2017...")
b04_2017_path = buscar_banda(carpeta_2017, "B04")  # RED
b08_2017_path = buscar_banda(carpeta_2017, "B08")  # NIR

print("📦 Buscando bandas en 2025...")
b04_2025_path = buscar_banda(carpeta_2025, "B04")  # RED
b08_2025_path = buscar_banda(carpeta_2025, "B08")  # NIR

print("🧮 Calculando NDVI 2017...")
ndvi_2017, profile = calcular_ndvi(b08_2017_path, b04_2017_path)

print("🧮 Calculando NDVI 2025...")
ndvi_2025, _ = calcular_ndvi(b08_2025_path, b04_2025_path)

# === Estadísticas ===
prom_2017 = np.nanmean(ndvi_2017)
prom_2025 = np.nanmean(ndvi_2025)
delta_ndvi = prom_2025 - prom_2017

print("📈 NDVI promedio 2017:", round(prom_2017, 3))
print("📉 NDVI promedio 2025:", round(prom_2025, 3))
print("🔁 Cambio promedio NDVI:", round(delta_ndvi, 3))

# === Mostrar gráfico comparativo ===
print("🖼️ Mostrando comparación...")
diferencia_ndvi = ndvi_2025 - ndvi_2017

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

im1 = axes[0].imshow(ndvi_2017, cmap='RdYlGn', vmin=-0.2, vmax=0.2)
axes[0].set_title("NDVI 2017")
plt.colorbar(im1, ax=axes[0])

im2 = axes[1].imshow(ndvi_2025, cmap='RdYlGn', vmin=-0.2, vmax=0.2)
axes[1].set_title("NDVI 2025")
plt.colorbar(im2, ax=axes[1])

im3 = axes[2].imshow(diferencia_ndvi, cmap='bwr', vmin=-0.2, vmax=0.2)
axes[2].set_title("Diferencia NDVI")
plt.colorbar(im3, ax=axes[2])

plt.tight_layout()
plt.show()

# === Guardar resultados ===
print("💾 Guardando resultados en carpeta 'data/results/'...")

# Actualizar perfil para guardar
profile.update(
    dtype=rasterio.float32,
    count=1,
    driver='GTiff'
)

# Guardar TIFFs
rasterio.open(os.path.join(result_dir, "ndvi_2017.tif"), "w", **profile).write(ndvi_2017.astype(rasterio.float32), 1)
rasterio.open(os.path.join(result_dir, "ndvi_2025.tif"), "w", **profile).write(ndvi_2025.astype(rasterio.float32), 1)
rasterio.open(os.path.join(result_dir, "diferencia_ndvi.tif"), "w", **profile).write(diferencia_ndvi.astype(rasterio.float32), 1)

# Guardar imágenes PNG
plt.imsave(os.path.join(result_dir, "ndvi_2017.png"), ndvi_2017, cmap='RdYlGn', vmin=-0.2, vmax=0.2)
plt.imsave(os.path.join(result_dir, "ndvi_2025.png"), ndvi_2025, cmap='RdYlGn', vmin=-0.2, vmax=0.2)
plt.imsave(os.path.join(result_dir, "diferencia_ndvi.png"), diferencia_ndvi, cmap='bwr', vmin=-0.2, vmax=0.2)

print("✅ Todo guardado correctamente en 'data/results/'")
