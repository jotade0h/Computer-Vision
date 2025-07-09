from ultralytics import YOLO
import cv2
import os
import numpy as np

# Ruta al modelo entrenado
model_path = "/content/runs/segment/train/weights/best.pt"
model = YOLO(model_path)

# Carpeta con los videos de entrada
input_folder = "/content/videos"
output_folder = "/content/videoresults"
os.makedirs(output_folder, exist_ok=True)

video_extensions = (".mp4", ".avi", ".mov", ".mkv")

# Zonas prohibidas
zona_1 = np.array([[1090, 100], [1110, 100], [920, 800], [750, 800]], dtype=np.int32)
zona_2 = np.array([[1155, 100], [1175, 100], [1480, 800], [1300, 800]], dtype=np.int32)
zonas = [zona_1, zona_2]

for filename in os.listdir(input_folder):
    if filename.lower().endswith(video_extensions):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"segmentado_{filename}")

        cap = cv2.VideoCapture(input_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        print(f"🎬 Procesando {filename}...")




        peligro_total = 0
        estado_anterior = False  # <== Faltaba esta inicialización
        zonas = [zona_1, zona_2]  # Asegúrate de haber definido zona_1 y zona_2 antes

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Realizar inferencia
            results = model.predict(
                source=frame,
                save=False,
                show=False,
                show_labels=False,
                show_conf=False
            )

            annotated_frame = results[0].plot()

            # Dibujar zonas prohibidas
            for zona in zonas:
                cv2.polylines(annotated_frame, [zona], isClosed=True, color=(0, 0, 255), thickness=3)

            # Inicializar bandera de peligro
            peligro = False

            # Obtener máscaras y clases detectadas
            masks = results[0].masks
            classes = results[0].boxes.cls.cpu().numpy().astype(int) if results[0].boxes else []

            if masks is not None:
              peligro = False  # Reiniciar en cada frame

              for i, mask in enumerate(masks.data.cpu().numpy()):
                  class_id = classes[i]

                  if class_id == 3:  # Vegetación
                      mask_binary = (mask * 255).astype(np.uint8)
                      mask_binary = cv2.resize(mask_binary, (width, height))  # Asegura que tamaño coincida

                      # Para cada zona
                      for zona in zonas:
                          zona_mask = np.zeros_like(mask_binary, dtype=np.uint8)
                          cv2.fillPoly(zona_mask, [zona], 255)

                          # Intersección entre zona y máscara
                          interseccion = cv2.bitwise_and(mask_binary, zona_mask)

                          if np.any(interseccion > 0):
                              peligro = True
                              break  # Sal de zonas
                  if peligro:
                      break  # Sal de máscaras


            # Mostrar en pantalla si hay peligro
            if peligro:
                cv2.putText(annotated_frame, "PELIGRO", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 0, 255), 4, cv2.LINE_AA)
                print("PELIGRO, guardando ubicación")
            else:
                cv2.putText(annotated_frame, "SEGURO", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (0, 255, 0), 4, cv2.LINE_AA)
                print("SEGURO")

            # Actualizar el contador si hubo un cambio de estado
            if peligro and not estado_anterior:
                peligro_total += 1
                estado_anterior = True
            elif not peligro:
                estado_anterior = False

            out.write(annotated_frame)

        cap.release()
        out.release()
        print(f"✅ Guardado: {output_path}")
        print(f"🔴 Total de eventos de PELIGRO en {filename}: {peligro_total}")