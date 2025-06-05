import cv2
from ultralytics import YOLO
import os
import csv
import sys

# Import webcam tool
sys.path.append("../webcam_capture")
from webcam import WebcamCapture, main as webcam_main  # import your webcam tool

def process_image(image_path, model_path, csv_path="box_counts.csv"):
    model = YOLO(model_path)
    CONF_THRESHOLD = 0.5
    MIN_BOX_AREA = 500

    img = cv2.imread(image_path)
    detections = model(img)[0].boxes

    count = 0
    for box in detections:
        conf = float(box.conf)
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        area = (x2 - x1) * (y2 - y1)
        if conf > CONF_THRESHOLD and area > MIN_BOX_AREA:
            count += 1
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.putText(img, f"Count: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Box Counter", img)
    print(f"[{os.path.basename(image_path)}] — {count} boxes detected. Press 'q' to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Image", "Box Count"])
        writer.writerow([os.path.basename(image_path), count])

    print(f"\n✅ CSV saved as: {csv_path}")

def main():
    model_path = "../yolov_11/yolov11_custom.pt"

    print("\n🎥 Choose image/video using webcam module...")
    file_path = webcam_main()  # this calls your original menu logic

    if not file_path:
        print("❌ No file selected or captured. Exiting.")
        return

    if file_path.lower().endswith((".jpg", ".jpeg", ".png")):
        process_image(file_path, model_path)
    else:
        print("⚠️ Video input detected — video processing not implemented yet.")
        # I can add video support if you confirm that’s needed

if __name__ == "__main__":
    main()

