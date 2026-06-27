# 🛣️ AI Pothole Detection System

An AI-powered road infrastructure monitoring system that automatically detects potholes from road images using YOLO, estimates damage severity, prioritizes repair urgency, and generates an intelligent road damage report with GPS location support.

---

## 📌 Project Overview

Road damage is a major cause of accidents and vehicle damage. This project uses Artificial Intelligence and Computer Vision to automatically detect potholes from uploaded road images and provide useful information for road maintenance authorities.

The system analyzes road images, classifies damage severity, assigns a repair priority, estimates repair cost, and displays the location on Google Maps.

---

## 🚀 Features

- ✅ AI-based pothole detection using YOLO
- ✅ Upload road images through a web interface
- ✅ Automatic pothole counting
- ✅ Damage severity analysis (Small / Medium / Large)
- ✅ Priority Ranking (Low / Medium / High / Critical)
- ✅ Estimated repair cost
- ✅ GPS location capture
- ✅ Google Maps integration
- ✅ Professional AI-generated road damage report
- ✅ Responsive Flask web application

---

## 🤖 AI Workflow

```text
Road Image
      │
      ▼
YOLO Object Detection Model
      │
      ▼
Detect Potholes
      │
      ▼
Calculate Severity
      │
      ▼
Priority Ranking
      │
      ▼
Estimate Repair Cost
      │
      ▼
Generate AI Road Damage Report
```

---

## 🛠️ Tech Stack

- Python
- Flask
- YOLO (Ultralytics)
- OpenCV
- PyTorch
- HTML
- CSS
- JavaScript
- Google Maps API (Location)
- Git
- GitHub

---

## 📂 Project Structure

```
AI-Pothole-Detection-System/
│
├── app.py
├── predict.py
├── predict_details.py
├── train.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
│   └── best.pt
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/USERNAME/AI-Pothole-Detection-System.git
```

Move into the project

```bash
cd AI-Pothole-Detection-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📊 Output

The system provides:

- Total Potholes
- Overall Severity
- Priority Ranking
- Estimated Repair Cost
- GPS Coordinates
- Google Maps Location
- AI Road Damage Report

---

## 📈 Future Enhancements

- Crack Detection
- Road Patch Detection
- PDF Report Generation
- Municipal Dashboard
- Real-time Camera Detection
- Video Processing
- PostgreSQL Database
- Leaflet GIS Dashboard
- Repair Recommendation Engine
- Mobile Application

---

## 👨‍💻 Author

**Sharau Jagtap**

MCA  
Vishwakarama University, Pune

GitHub:
https://github.com/sharau09

LinkedIn:
https://www.linkedin.com/in/sharau-jagtap-2b1080248

---

## ⭐ If you found this project useful, consider giving it a star.
