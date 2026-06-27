from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(
    data="dataset/data.yaml",
    epochs=30,
    imgsz=640,
    batch=8,
    device="mps",
    workers=0
)
