# 📦 Warehouse Box Counter - YOLOv8 Object Detection

This project uses YOLOv8 to detect boxes in a warehouse setup. 
It includes the trained model and all required files to test and run object detection on a custom dataset.

---

## 📁 Repository Structure


warehouse-box-counter-cv/

└── yolov8/

    ├── runs/
    
    ├── train/
    
    ├── val/
    
    ├── classes.txt
    
    ├── data_custom.yaml
    
    ├── download_image.py
    
    ├── test.py
    
    ├── yolov8m.pt
    
    ├── yolov8m_custom.onnx
    
    └── yolov8m_custom.pt (best.pt)
    
✅ Steps to Run the Model on Your System

### 1. Clone the Repository
📌 Open Command Prompt and navigate to your desired working directory.

C:\Users\GANJA SRIVIDYA>cd C:\Users\GANJA SRIVIDYA\Videos\testing1

C:\Users\GANJA SRIVIDYA\Videos\testing1> git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git

### 2. Navigate to the yolov8 Directory
C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv>cd yolov8

### 3. Create a Virtual Environment
C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv\yolov8>python -m venv venv_yolo

### 4. Activate the Virtual Environment
For Windows Command Prompt:

C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv\yolov8>venv_yolo\Scripts\activate

after activating

(venv_yolo) C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv\yolov8>

### 6. Install Required Libraries

Install all dependencies using the requirements.txt file:

(venv_yolo) C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv\yolov8>pip install -r requirements.txt

### 7. Run the Model

Now run the testing script:

(venv_yolo) C:\Users\GANJA SRIVIDYA\Videos\testing1\warehouse-box-counter-cv\yolov8>python test.py

to run on custom images/videos

add the path of the multimedia in place of warehouse.jpg in the source of test.py file 

### 8.To see the results

Go to your cloned folder yolov8\runs\detect

### 9.To deactivate the virtual environment, simply run:

deactivate
