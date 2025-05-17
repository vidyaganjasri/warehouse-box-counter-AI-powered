import cv2
import os
from datetime import datetime

# 🔁 Import capture/upload tool from Task 1
from webcam_capture import main as get_input_file


class PreProcessor:
    def __init__(self):
        pass

    def load_image(self, path):
        if not path or not os.path.exists(path):
            print("❌ Invalid image path.")
            return None, None
        image = cv2.imread(path)
        print(f"📥 Processing image: {path}")
        return image, path

    def convert_to_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_blur(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    def detect_edges(self, image):
        return cv2.Canny(image, 50, 150)

    def find_and_draw_boxes(self, original, edges):
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        box_count = 0

        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            area = cv2.contourArea(cnt)
            if len(approx) == 4 and area > 1000:
                cv2.drawContours(original, [approx], 0, (0, 255, 0), 2)
                box_count += 1

        return original, box_count

    def annotate_frame(self, frame, box_count):
        cv2.putText(frame, f"Boxes Detected: {box_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        return frame

    def show_results(self, result_img, edges):
        cv2.imshow("Detected Boxes", result_img)
        cv2.imshow("Edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process_image(self, image_path):
        image, _ = self.load_image(image_path)
        if image is None:
            return

        original = image.copy()
        gray = self.convert_to_grayscale(image)
        blurred = self.apply_blur(gray)
        edges = self.detect_edges(blurred)
        result, box_count = self.find_and_draw_boxes(original, edges)
        annotated = self.annotate_frame(result, box_count)
        self.show_results(annotated, edges)

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("❌ Failed to open video.")
            return

        print("📽️ Processing video frames... Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            original = frame.copy()
            gray = self.convert_to_grayscale(frame)
            blurred = self.apply_blur(gray)
            edges = self.detect_edges(blurred)
            result, box_count = self.find_and_draw_boxes(original, edges)
            annotated = self.annotate_frame(result, box_count)

            cv2.imshow("📦 Boxes in Video", annotated)
            cv2.imshow("Edges", edges)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


def main():
    # Get input file path from Task 1 (webcam capture/upload)
    path = get_input_file()
    if not path:
        print("⚠️ No file path received from Task 1.")
        return

    processor = PreProcessor()

    # Determine if the input is an image or video
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        processor.process_image(path)
    elif path.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        processor.process_video(path)
    else:
        print("❌ Unsupported file format. Please provide an image or video.")


if __name__ == "__main__":
    main()
