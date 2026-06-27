from flask import Flask, render_template, request
from ultralytics import YOLO
import os
import shutil

app = Flask(__name__)

model = YOLO("model/best.pt")

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    model.predict(filepath, save=True, conf=0.25)

    latest_folder = sorted(
        [f for f in os.listdir("runs/detect") if f.startswith("predict")],
        key=lambda x: os.path.getmtime(os.path.join("runs/detect", x))
    )[-1]

    result_image = file.filename

    source_image = os.path.join(
        "runs/detect",
        latest_folder,
        result_image
    )

    destination_image = os.path.join(
        RESULT_FOLDER,
        result_image
    )

    if os.path.exists(source_image):
        shutil.copy(source_image, destination_image)

    return render_template(
        "result.html",
        image=result_image
    )


if __name__ == "__main__":
    app.run(debug=True)
