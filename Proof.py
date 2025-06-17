from ultralytics import YOLO

# Cargar el modelo preentrenado (ajusta la ruta del modelo si es necesario)
model = YOLO('C:/Users/jdoso/Desktop/Yolov8/runs/mlflow/386623390962322669/8e6f9f07a8d04c88b972f58666a9dc80/artifacts/weights/best.pt')  # Reemplaza 'best.pt' con la ruta a tus pesos entrenados

# Ruta al conjunto de test
test_images = 'C:/Users/jdoso/Desktop/Yolov8/Fruits3/test/images'  # Reemplaza con la ruta de tu conjunto de imágenes de prueba

# Realiza las predicciones en el conjunto de test
results = model(test_images, save=True)  # 'save=True' guarda las predicciones en un directorio

# Mostrar las métricas de evaluación (como mAP, precisión, recall)
metrics = model.val()

# Acceder a las métricas directamente
print("Evaluación del conjunto de test:")
print(f"Precisión (P): {metrics.box.map50}")
print(f"Recall (R): {metrics.box.map}")
print(f"mAP@0.5: {metrics.box.map50}")
print(f"mAP@0.5:0.95: {metrics.box.map}")
