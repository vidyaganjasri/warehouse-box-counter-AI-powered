from ultralytics import YOLO
import cv2
import WEBCAM_CAPTURE.webcam_capture 
# Import webcam_capture directly since it's in the same folder

# ======= PATH CONFIG =======
IMAGE_PATH = "C:\\Users\\HP\\Desktop\\warehouse-box-counter-cv\\warehouse-box-counter-cv\\yolov8\\warehouse.jpg"
VIDEO_PATH = "C:\\Users\\HP\\Desktop\\warehouse-box-counter-cv\\warehouse-box-counter-cv\\yolov8\\box.mp4"
MODEL_PATH = "yolov8/yolov8m_custom.pt"
OUTPUT_IMAGE = "counted_boxes_output.jpg"
OUTPUT_VIDEO = "counted_boxes_output_video.mp4"
CONF_THRESHOLD = 0.7
# ===========================

# === Ask user for mode ===
print("Select mode:")
print("1. Image (from file)")
print("2. Video (from file)")
print("3. Webcam Image Capture / Upload")
print("4. Webcam Video Capture / Upload")
mode = input("Enter choice (1/2/3/4): ").strip()

# === Load model ===
model = YOLO(MODEL_PATH)
class_names = model.names
print(f"📋 Class names: {class_names}")

def process_frame(frame):
    results = model(frame, conf=0.85, iou=0.4)[0]
    boxes = results.boxes
    box_count = 0

    for box in boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        if conf < CONF_THRESHOLD:
            continue

        class_name = class_names[cls_id]
        if class_name.lower() == 'box':
            box_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = f"{class_name} {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.putText(frame, f"Total Boxes: {box_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
    return frame, box_count

if mode == "1":
    # IMAGE FROM FILE
    frame = cv2.imread(IMAGE_PATH)
    processed_frame, count = process_frame(frame)
    print(f"🟦 Total Boxes Detected: {count}")
    cv2.imwrite(OUTPUT_IMAGE, processed_frame)
    cv2.imshow("Detected Boxes", processed_frame)
    print("🔍 Press 'q' to close the image window.")
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

elif mode == "2":
    # VIDEO FROM FILE
    cap = cv2.VideoCapture(VIDEO_PATH)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        processed_frame, count = process_frame(frame)
        out.write(processed_frame)
        cv2.imshow("Detected Boxes", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("✅ Video processing completed and saved.")

elif mode == "3":
    # WEBCAM IMAGE CAPTURE / UPLOAD
    img_path = WEBCAM_CAPTURE.webcam_capture.main()  # call your webcam_capture script main function
    if img_path:
        frame = cv2.imread(img_path)
        processed_frame, count = process_frame(frame)
        print(f"📸 Webcam Image - Boxes Detected: {count}")
        cv2.imshow("Detected Boxes", processed_frame)
        print("🔍 Press 'q' to close the image window.")
        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()
    else:
        print("❌ No image captured or uploaded.")

elif mode == "4":
    # WEBCAM VIDEO CAPTURE / UPLOAD
    video_path = WEBCAM_CAPTURE.webcam_capture.main()  # call your webcam_capture script main function
    if video_path:
        cap = cv2.VideoCapture(video_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(OUTPUT_VIDEO, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            processed_frame, count = process_frame(frame)
            out.write(processed_frame)
            cv2.imshow("Detected Boxes", processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        print("✅ Webcam video processed and saved.")
    else:
        print("❌ No video captured or uploaded.")

else:
    print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
