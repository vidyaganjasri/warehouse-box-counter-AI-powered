import cv2
import os
from datetime import datetime


class ImageLoader:
    def __init__(self, folder="captures"):
        self.folder = folder

    def get_latest_image_path(self):
        files = sorted(
            [f for f in os.listdir(self.folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))],
            key=lambda x: os.path.getmtime(os.path.join(self.folder, x)),
            reverse=True
        )
        if not files:
            print("❌ No image files found in the captures folder.")
            return None
        return os.path.join(self.folder, files[0])

    def load_image(self):
        image_path = self.get_latest_image_path()
        if not image_path:
            return None, None
        image = cv2.imread(image_path)
        print(f"📥 Processing image: {image_path}")
        return image, image_path


class PreProcessor(ImageLoader):
    def __init__(self, folder="captures"):
        super().__init__(folder)

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
    processor = PreProcessor()

    image, _ = processor.load_image()
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
