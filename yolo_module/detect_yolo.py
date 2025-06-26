from ultralytics import YOLO
import os

# Get absolute path to current script (detect_yolo.py)
base_dir = os.path.dirname(os.path.dirname(__file__))  # Go up one level to project root
model_path = os.path.join(base_dir, "yolo_module", "best.pt")

# Check and load
if not os.path.exists(model_path):
    raise FileNotFoundError(f"'best.pt' not found at: {model_path}")

model = YOLO(model_path)  # ✅ Proper model object

def detect_boxes(frame):
    """
    Accepts a BGR image frame.
    Returns a list of bounding boxes in (x, y, w, h, class_id, confidence) format.
    """
    results = model.predict(source=frame, conf=0.5, verbose=False)

    boxes = []
    for r in results:
        for box, cls_id, conf in zip(r.boxes.xyxy, r.boxes.cls, r.boxes.conf):
            x1, y1, x2, y2 = map(int, box[:4])
            w, h = x2 - x1, y2 - y1
            boxes.append((x1, y1, w, h, int(cls_id), float(conf)))
    return boxes
