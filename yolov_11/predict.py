from ultralytics import YOLO

model = YOLO("yolov11_custom.pt")

model.predict(source='9.jpg', show=True, save=True, conf=0.3,
line_width=2,save_crop=True, save_txt=True, hide_labels=False, hide_conf=False)
