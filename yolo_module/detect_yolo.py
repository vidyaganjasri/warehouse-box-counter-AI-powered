from ultralytics import YOLO
import cv2
import os

# Load the model from correct absolute path using raw string
#model = YOLO(r'C:\Users\GANJA SRIVIDYA\Music\warehouse-box-counter-cv\yolo_module\best.pt')
model = YOLO(r'C:\Users\GANJA SRIVIDYA\Documents\kaggle\working\runs\detect\train2\weights\best.pt')


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
