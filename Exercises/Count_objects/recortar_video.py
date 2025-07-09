from moviepy.editor import VideoFileClip
import os

# Parámetros
video_path = "C:/Users/jdoso/Downloads/segmentado_loco_02.mp4"  # Cambia por el path real
segundo_inicio = 10  # X
segundo_fin = 62     # Y

# Cargar video original
video = VideoFileClip(video_path)

# Crear video recortado
video_recortado = video.subclip(segundo_inicio, segundo_fin)

# Nombre de salida
base, ext = os.path.splitext(video_path)
recorte_path = f"{base}_recortado_{segundo_inicio}_a_{segundo_fin}{ext}"

# Guardar video recortado
video_recortado.write_videofile(recorte_path, codec="libx264")

print(f"Video original: {video_path}")
print(f"Video recortado guardado en: {recorte_path}")