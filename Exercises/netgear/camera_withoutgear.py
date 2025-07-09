import cv2
from dotenv import load_dotenv
import os

# 🔄 Cargar variables desde .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Obtener las variables
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")
url = os.getenv("CAMERA_URL")




capture = cv2.VideoCapture(url) #Camaras
# capture = cv2.VideoCapture('rtsp://administrador:william1560@192.168.128.3:554/stream1') camara abajo
# rtsp://administrador:william1560@192.168.128.3:554/stream1

#capture = cv2.VideoCapture("rtsp://usuario:***ADMIN@192.168.12813/video")


while True:
    ret, frame = capture.read()
    cv2.imshow('captura', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

#try