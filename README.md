
````markdown
# 📦 Warehouse Box Counter – A Computer Vision Project

**Warehouse Box Counter** is a Python-based computer vision project designed to automatically **detect and count boxes** in warehouse images and videos using the **YOLOv11** object detection model.

This project was developed by a team of students to simplify and automate inventory estimation in warehouse settings. It works with **images, webcam input, or video streams** and visually marks each detected box with bounding boxes while also displaying the total count — all through a clean and interactive graphical interface built with **Tkinter**.

Whether you're experimenting with object detection, learning computer vision, or building smart warehouse applications — this project serves as a practical example of how AI can streamline real-world logistics.

---

## ✨ Features

- 📷 Detect boxes from webcam, images, or videos  
- 🧠 YOLOv11-based object detection  
- 🎯 Display bounding boxes and total count  
- 🖥️ Easy-to-use interface with Tkinter GUI  

---

## 🚀 How to Run

### 1. Clone the Repository

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

## 📁 Folder Structure

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

## ⚙️ Tech Stack

| Tool/Tech | Purpose              |
| --------- | -------------------- |
| Python    | Programming Language |
| YOLOv11   | Object Detection     |
| Tkinter   | GUI Framework        |
| OpenCV    | Image Processing     |

---

## 👩‍💻 Contributors

* [@MANASA-NUKALA](https://github.com/MANASA-NUKALA)
* [@vidyaganjasri](https://github.com/vidyaganjasri)
* [@MissHaRin19](https://github.com/MissHaRin19)
* [@AdulaAnusha22](https://github.com/AdulaAnusha22)
* [@KPRANEETHA-1](https://github.com/KPRANEETHA-1)
* [@Sudheshna193](https://github.com/Sudheshna193)

```
---
```
