from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

results = model("test_images/pothole1.jpg")

for r in results:
    for box in r.boxes:
        print("Class:", int(box.cls))
        print("Confidence:", float(box.conf))
