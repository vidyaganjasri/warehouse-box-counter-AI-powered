import sys
import os
sys.path.append(os.path.abspath('../WEBCAM_CAPTURE'))
from webcam_capture import main as get_input_file
from ultralytics import YOLO

def run_yolo_detection():
    image_path = get_input_file()
    if image_path is None:
        print("❌ No image was captured.")
        return None
    
    model = YOLO("yolov8m_custom.pt")
    results = model.predict(source=image_path, conf=0.85, line_thickness=1, save=True, show=True)
    return results

if __name__ == "__main__":
    run_yolo_detection()
