import cv2
import os

# Path to the captured image
image_path = "captures/image_20250511_180917.jpg"  # Replace with your actual image name

# Check if the image exists
if not os.path.exists(image_path):
    print(f"❌ Error: Unable to read image at {image_path}")
    exit()

# Load the image
image = cv2.imread(image_path)
original = image.copy()

# Step 1: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 2: Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 3: Detect edges using Canny
edges = cv2.Canny(blurred, 50, 150)

# Step 4: Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

box_count = 0

# Step 5: Filter for rectangular boxes based on shape and size
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
    area = cv2.contourArea(cnt)
    if len(approx) == 4 and area > 1000:  # Check if shape is rectangular and not too small
        cv2.drawContours(original, [approx], 0, (0, 255, 0), 2)
        box_count += 1

# Step 6: Display box count
cv2.putText(original, f"Boxes Detected: {box_count}", (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Step 7: Show result
cv2.imshow("Detected Boxes", original)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
