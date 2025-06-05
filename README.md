# 📦 Warehouse Box Counter - CV-Based Application

Welcome to our team project — a simple and effective tool that helps **automatically detect and count boxes** in warehouse images using **YOLOv11** and a user-friendly Python GUI.

Whether you're working with **live webcam feed**, **uploaded images**, or even **video files**, this application handles it smoothly and displays the result with bounding boxes and the total count — all from a single interface.

---

## 🛠️ Getting Started

Want to try it out on your system? Just follow these steps to get up and running.

### 1. Clone the Repository

Start by cloning the project to your local machine:

```bash
git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git
cd warehouse-box-counter-cv
2. Create and Activate a Virtual Environment
It’s always a good idea to keep dependencies isolated. Here’s how:

For Windows

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
For macOS/Linux

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Required Dependencies
Now install all the necessary packages using:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Application
Once setup is done, go into the GUI folder and start the app:

bash
Copy
Edit
cd gui
python app_gui.py
You’ll now see a simple interface to upload images or use the webcam/video for detection.

📁 Project Structure
bash
Copy
Edit
warehouse-box-counter-cv/
├── gui/                 # GUI interface (main entry point: app_gui.py)
├── webcam_capture/      # Scripts for capturing images using webcam
├── yolov8/              # YOLOv8 model weights and config
├── yolo_module/         # YOLO detection-related scripts
├── preprocessing/       # Optional image pre-processing
├── box_counter/         # Core logic for counting boxes
├── detect_contours.py   # Alternative box detection using contours
├── main.py              # Initial script before GUI integration
├── requirements.txt     # List of Python dependencies
└── README.md            # You're here!
⚙️ Tech Stack Used
Programming Language: Python

Object Detection Model: YOLOv11 (via Ultralytics)

GUI Framework: Tkinter

Computer Vision Library: OpenCV

👥 Team Contributors
This project was built with teamwork and collaboration. Huge thanks to:

@MANASA-NUKALA

@vidyaganjasri

@MissHaRin19

@AdulaAnusha22

@KPRANEETHA-1

@Sudheshna193

📌 Notes
Make sure your webcam permissions are enabled when using the live feed mode.

YOLOv11 models and weights must be pre-downloaded into the yolov8/ folder.

Performance may vary based on hardware — use GPU if available for faster inference.

🏁 License
This project is licensed under the MIT License.




















