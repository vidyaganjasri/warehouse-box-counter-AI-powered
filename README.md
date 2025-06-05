

````markdown
# 📦 Warehouse Box Counter - CV Based Application

A team project to automatically **detect and count boxes** in warehouse images using **YOLOv8** and **Python GUI**. The system uses live webcam or uploaded images, integrates with a YOLOv8 model, and provides a clean GUI interface for non-technical users.

---

## 🛠️ Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git
cd warehouse-box-counter-cv
````

### 2. Create a Virtual Environment

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

> ⚠️ Navigate to the `gui/` folder and run the GUI script.

```bash
cd gui
python app_gui.py
```

---

## 📂 Project Structure

```plaintext
warehouse-box-counter-cv/
├── gui/                 # Main GUI application (run app_gui.py)
├── webcam_capture/      # Webcam image capture script
├── yolov8/              # YOLOv8 pretrained model folder
├── yolo_module/         # YOLO detection wrapper scripts
├── preprocessing/       # Preprocessing utilities
├── box_counter/         # Box counting logic
├── detect_contours.py   # (Optional) contour-based detection
├── main.py              # Previous combined logic (non-GUI)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧠 Tech Stack

* **Language:** Python
* **Model:** YOLOv8 (via Ultralytics)
* **GUI:** Tkinter
* **Vision:** OpenCV

---

## 👥 Contributors

* @MANASA-NUKALA
* @vidyaganjasri
* @AdulaAnusha22
* @Sudheshna193
* @KPRANEETHA-1
* @MissHaRin19

---

## 📝 License

This project is not currently licensed. Please contact the maintainers for permissions or contributions.

```

---

Let me know if you want to include:

- Sample screenshots  
- Demo video link  
- Setup troubleshooting tips  

I'm happy to help include those too.
```
