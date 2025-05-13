from ultralytics import YOLO
model = YOLO("yolov8m_custom.pt")

model.predict(source='warehouse.jpg',show=True,save=True,conf=0.85,line_thickness=1)
