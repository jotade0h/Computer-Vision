from ultralytics import YOLO
from dotenv import load_dotenv
import os
import cv2
import cvzone

# 🔄 Cargar variables desde .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Obtener las variables
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")
url = os.getenv("CAMERA_URL")

cap=cv2.VideoCapture(url)

CAMERA_URL = os.getenv("CAMERA_URL")


if CAMERA_URL is None:
    print("⚠️ No se encontró la variable CAMERA_URL en el .env")

while True:
    success, img = cap.read()
    if not success:
        print("❌ No se pudo leer la imagen desde la cámara.")
        break

    cv2.imshow('Image', img)

    # Espera 1 milisegundo y captura la tecla presionada
    key = cv2.waitKey(1) & 0xFF

    # Presiona 'q' para salir
    if key == ord('q'):
        print("🔚 Saliendo del programa...")
        break

# Libera la cámara y cierra la ventana
cap.release()
cv2.destroyAllWindows()