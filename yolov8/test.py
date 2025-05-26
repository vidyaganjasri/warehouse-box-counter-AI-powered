import sys
import os

# Add absolute path to WEBCAM_CAPTURE to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
webcam_path = os.path.join(parent_dir, "WEBCAM_CAPTURE")
sys.path.append(webcam_path)

# Import webcam_capture module
from webcam_capture import main as get_input_file
sys.path.append(os.path.abspath('../webcam_capture'))

from webcam import main as get_input_file

from ultralytics import YOLO

def run_yolo_detection():
    image_path = get_input_file()  # This should return the path of a captured image
    if image_path is None:
        print("❌ No image was captured.")
        return None
    
    model = YOLO("yolov8/yolov8m_custom.pt")
 # Make sure this path is correct
    results = model.predict(
        source=image_path,
        conf=0.85,
        line_thickness=1,
        save=True,
        show=True
    )
    return results

if __name__ == "__main__":
    run_yolo_detection()
