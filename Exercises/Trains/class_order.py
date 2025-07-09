from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO("/content/runs/segment/train/weights/best.pt")

# Mostrar clases y su índice
for idx, class_name in model.names.items():
    print(f"{idx}: {class_name}")