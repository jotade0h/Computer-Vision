import subprocess
import imageio_ffmpeg as ffmpeg  # ✅ usa el ffmpeg incluido en Python

ffmpeg_path = ffmpeg.get_ffmpeg_exe()  # obtiene la ruta real al binario

input_file = "C:/Users/jdoso/Desktop/Yolov8/Train/videos/loco.avi"
output_file = "C:/Users/jdoso/Desktop/Yolov8/Train/videos/loco.mp4"

subprocess.run([
    ffmpeg_path,
    "-i", input_file,
    "-c:v", "copy",
    "-c:a", "copy",
    output_file
])