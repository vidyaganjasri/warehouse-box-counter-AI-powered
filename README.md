````markdown
# Warehouse Box Counter – A Computer Vision Project

**Warehouse Box Counter** is a Python-based computer vision project that automatically detects and counts boxes in warehouse images and videos using the YOLOv11 object detection model.

Developed by a team of students, the project aims to simplify inventory estimation in warehouse environments. It supports detection from images, webcam input, and video streams. Each box is highlighted with bounding boxes and the total count is displayed through an intuitive graphical interface built with Tkinter.

This project is a practical example of how artificial intelligence and computer vision can assist in real-world logistics and automation tasks.

---

## Features

- Detect boxes from webcam, images, or videos  
- YOLOv11-based object detection  
- Displays bounding boxes and total count  
- Simple user interface using Tkinter GUI  

---

### How to Run

#### 1. Clone the Repository

```bash
git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git
cd warehouse-box-counter-cv
````

### 2. Create a Virtual Environment

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Launch the Application

```bash
cd gui
python app_gui.py
```

---

## Project Structure

```
warehouse-box-counter-cv/
├── box/                  → Model weights or checkpoint files
├── box_counter/          → Core logic to count boxes
├── gui/                  → Graphical interface (launch app_gui.py here)
├── preprocessing/        → Image preprocessing scripts
├── webcam_capture/       → Scripts for capturing webcam input
├── yolo_module/          → YOLO detection logic
├── Testing2.0/           → Updated GUI and test images
├── detect_contours.py    → Contour-based detection (OpenCV)
├── main.py               → Original non-GUI detection script
├── testing.py            → GUI and model test script
├── requirements.txt      → Dependencies list
└── README.md             → Project documentation
```

---

## Tech Stack

| Technology | Purpose              |
| ---------- | -------------------- |
| Python     | Programming language |
| YOLOv11    | Object detection     |
| Tkinter    | GUI framework        |
| OpenCV     | Image processing     |

---

## Contributors

* [@MANASA-NUKALA](https://github.com/MANASA-NUKALA)
* [@vidyaganjasri](https://github.com/vidyaganjasri)
* [@MissHaRin19](https://github.com/MissHaRin19)
* [@AdulaAnusha22](https://github.com/AdulaAnusha22)
* [@KPRANEETHA-1](https://github.com/KPRANEETHA-1)
* [@Sudheshna193](https://github.com/Sudheshna193)

````
---
````
