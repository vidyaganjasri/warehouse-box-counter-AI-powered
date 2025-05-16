import cv2
import os
from datetime import datetime

# 🔁 Import the capture/upload tool from Task 1
from webcam_capture import main as get_input_file


class PreProcessor:
    def __init__(self):
        pass  # No need for folder parameter anymore

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

    def annotate_and_show(self, result_img, edges, box_count):
        cv2.putText(result_img, f"Boxes Detected: {box_count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Detected Boxes", result_img)
        cv2.imshow("Edges", edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    # 🔁 Get input image path from Task 1 (webcam_capture.py)
    image_path = get_input_file()
    if image_path is None:
        return

    processor = PreProcessor()
    image, _ = processor.load_image(image_path)
    if image is None:
        return

    original = image.copy()
    gray = processor.convert_to_grayscale(image)
    blurred = processor.apply_blur(gray)
    edges = processor.detect_edges(blurred)
    result, box_count = processor.find_and_draw_boxes(original, edges)
    processor.annotate_and_show(result, edges, box_count)


if __name__ == "__main__":
    main()
