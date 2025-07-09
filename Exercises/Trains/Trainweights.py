import torch
from ultralytics import YOLO

torch.cuda.empty_cache()

model = YOLO("yolov8m-seg.pt")  # También puedes probar yolov8s-seg.pt si tienes más GPU

model.train(
    data="/content/seisrename/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16  # Usa GPU
)