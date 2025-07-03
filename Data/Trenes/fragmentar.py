import subprocess
import os
import imageio_ffmpeg as ffmpeg


input_file = "C:/Users/jdoso/Desktop/Yolov8/Train/videos/loco.avi"
output_pattern = "C:/Users/jdoso/Desktop/Yolov8/Train/videos/loco_%02d.mp4"


ffmpeg_path = ffmpeg.get_ffmpeg_exe()

subprocess.run([
    ffmpeg_path,
    "-i", input_file,
    "-c", "copy",               # sin recodificación (más rápido)
    "-map", "0",                # asegura que toma todas las pistas
    "-f", "segment",            # modo segmentación
    "-segment_time", "60",      # cada 60 segundos
    "-reset_timestamps", "1",   # reinicia timestamps en cada fragmento
    output_pattern
])
