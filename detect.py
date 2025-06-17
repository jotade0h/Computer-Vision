from ultralytics import YOLO

# 1. Cargar el modelo preentrenado (por ejemplo, YOLOv8n)
model = YOLO('yolov8n.pt')  # También podrías usar yolov8s.pt, yolov8m.pt, etc.

# 2. Entrenar el modelo
# Los parámetros importantes son la ruta al archivo .yaml de los datos, el número de épocas y el tamaño de las imágenes
results = model.train(data='C:/Users/jdoso/Desktop/Yolov8/Fruits3/data.yaml', epochs=100, imgsz=640, batch=16, lr0=0.0005)

# 3. Evaluar el modelo entrenado (opcional)
metrics = model.val()
