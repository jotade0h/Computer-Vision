# count_motos_rtsp.py
# -*- coding: utf-8 -*-

import cv2
import time
from ultralytics import YOLO
from utils import draw_boxes, count_objects

model=YOLO("yolov8n.pt")



from dotenv import load_dotenv
import os

# 🔄 Cargar variables desde .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Obtener las variables
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")
url = os.getenv("CAMERA_URL")




cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error al conectar con la camara")
    exit()

# Coordenadas del ROI
x1, x2 = 150, 610
y1, y2 = 40, 360
cx_linea = int((x2 - x1) / 2)

# Parametros para conteo
fps_deseado = 2
intervalo = int(30 / fps_deseado)
frame_count = 0
conteo_izq_der = 0
conteo_der_izq = 0
ids_contados = set()
historico = {}

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Mostrar solo para ver contexto
    view = frame.copy()
    cv2.rectangle(view, (x1, y1), (x2, y2), (0, 255, 0), 1)
    cv2.line(view, (x1 + cx_linea, y1), (x1 + cx_linea, y2), (0, 0, 255), 1)
    cv2.imshow("Vista", view)

    if frame_count % intervalo == 0:
        roi = frame[y1:y2, x1:x2]
        roi_resized = cv2.resize(roi, (320, 180))  # resoluciÃ³n mÃ¡s baja
        results = model.track(roi_resized, persist=True, verbose=False)[0]

        if results.boxes.id is not None:
            ids = results.boxes.id.int().tolist()
            cls = results.boxes.cls.int().tolist()
            boxes = results.boxes.xyxy.tolist()

            for i, track_id in enumerate(ids):
                label = model.names[cls[i]]
                if label not in ["person", "car", "motorbike"]:
                    continue

                x_min, y_min, x_max, y_max = boxes[i]
                cx = int((x_min + x_max) / 2)

                if track_id in historico:
                    anterior = historico[track_id]
                    if anterior < cx_linea < cx and track_id not in ids_contados:
                        conteo_izq_der += 1
                        ids_contados.add(track_id)
                        print(f"{label} izquierda ? derecha")
                    elif anterior > cx_linea > cx and track_id not in ids_contados:
                        conteo_der_izq += 1
                        ids_contados.add(track_id)
                        print(f"{label} derecha ? izquierda")
                historico[track_id] = cx

        print(f"Izq?Der: {conteo_izq_der}, Der?Izq: {conteo_der_izq}")

    frame_count += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
