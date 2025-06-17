import cv2
from ultralytics import YOLO

# Cargar el modelo YOLO con los pesos que ya tienes
model = YOLO('C:/Users/jdoso/Desktop/Yolov8/runs/mlflow/386623390962322669/35fc0a7c04d34b59990689fa73332656/artifacts/weights/best.pt')

# Abrir el video
video_path = 'C:/Users/jdoso/Desktop/Yolov8/Fruits.mp4'
cap = cv2.VideoCapture(video_path)

# Obtener detalles del video original
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Dimensiones deseadas para la ventana pequeña
window_width = 1080  # Ancho de la ventana
window_height = 720  # Alto de la ventana

# Configurar el codec y el writer para guardar el video con las predicciones
output_path = 'C:/Users/jdoso/Desktop/Yolov8/Fruits_run0.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para guardar en formato MP4
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))  # Usamos el tamaño original para guardar

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Hacer la predicción en cada frame
    results = model(frame)

    # Dibujar las predicciones en el frame
    annotated_frame = results[0].plot()

    # Guardar el frame original con las predicciones (mantiene el tamaño original)
    out.write(annotated_frame)

    # Redimensionar el frame para mostrarlo en una ventana más pequeña
    resized_frame = cv2.resize(annotated_frame, (window_width, window_height))

    # Mostrar el frame redimensionado con las predicciones
    cv2.imshow('Predicciones YOLO (Ventana pequeña)', resized_frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()