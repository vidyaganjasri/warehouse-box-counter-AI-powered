from ultralytics import YOLO
import cv2

# Load the model once when the module is imported
model = YOLO("yolov8/yolov8m_custom.pt")  # or yolov8n.pt for default testing

def detect_boxes(frame):
    """
    Accepts a BGR image frame.
    Returns a list of bounding boxes in (x, y, w, h) format.
    """
    results = model.predict(source=frame, conf=0.5, verbose=False)

    boxes = []
    for r in results:
        for box in r.boxes.xyxy:  # bounding box in [x1, y1, x2, y2]
            x1, y1, x2, y2 = map(int, box[:4])
            w, h = x2 - x1, y2 - y1
            boxes.append((x1, y1, w, h))
    return boxes
