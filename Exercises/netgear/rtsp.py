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

cap = cv2.VideoCapture(url) #Camaras


while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()