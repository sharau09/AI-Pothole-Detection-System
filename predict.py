from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

results = model.predict(
    source="dataset/test/images",
    save=True,
    conf=0.25
)

print("Prediction Complete")

