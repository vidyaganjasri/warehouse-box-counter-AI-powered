import sys
import os
sys.path.append(os.path.abspath('../WEBCAM_CAPTURE'))

from webcam_capture import main as get_input_file
from ultralytics import YOLO

image_path = get_input_file()
if image_path is None:
    print("❌ No image was captured.")
    exit()

model = YOLO("yolov8m_custom.pt")
model.predict(source=image_path, show=True, save=True, conf=0.85, line_thickness=1)
