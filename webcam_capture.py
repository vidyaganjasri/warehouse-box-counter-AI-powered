import cv2
from datetime import datetime
import os
import time

# Step 1: Create output folder if it doesn't exist
output_dir = "captures"
os.makedirs(output_dir, exist_ok=True)

# Step 2: Generate timestamped filename
def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# Step 3: Capture image
def capture_image(cap):
    print("📷 Image capture mode: Press SPACE to capture the image. Press ESC to cancel.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame.")
            break

        # Show the webcam preview
        cv2.imshow("📸 Live Preview - Press SPACE to capture", frame)

        key = cv2.waitKey(1)

        if key == 27:  # ESC key to cancel
            print("❌ Canceled.")
            break
        elif key == 32:  # SPACE key to capture
            filename = f"{output_dir}/image_{get_timestamp()}.jpg"
            cv2.imwrite(filename, frame)
            print(f"✅ Image saved as: {filename}")
            break

# Step 4: Record video
def record_video(cap):
    print("🎥 Video recording mode: Press 'S' to start and 'E' to end the recording.")

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    filename = f"{output_dir}/video_{get_timestamp()}.avi"
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    recording = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame.")
            break

        # Show the webcam preview while recording
        if recording:
            out.write(frame)
            cv2.imshow("🎥 Live Recording - Press 'E' to stop", frame)
        else:
            cv2.imshow("🎥 Live Preview - Press 'S' to start recording", frame)

        key = cv2.waitKey(1)

        if key == 27:  # ESC key to cancel
            print("❌ Canceled.")
            break
        elif key == ord('s') and not recording:  # 'S' to start recording
            recording = True
            print("✅ Recording started.")
        elif key == ord('e') and recording:  # 'E' to stop recording
            recording = False
            print("🛑 Recording stopped.")
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"✅ Video saved as {filename}")

# Step 5: Main menu for choosing action
def main():
    # Initialize webcam capture
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("❌ Error: Cannot open webcam.")
        return

    # Wait for webcam to initialize
    time.sleep(1)

    # Show options to user
    print("\n📷 Webcam Capture Tool")
    print("1. Capture Image")
    print("2. Record Video")
    choice = input("Enter 1 or 2 to choose: ")

    if choice == '1':
        capture_image(cap)
    elif choice == '2':
        record_video(cap)
    else:
        print("❌ Invalid choice. Please choose 1 or 2.")

    cap.release()
    cv2.destroyAllWindows()

# Run the main function
if __name__ == "__main__":
    main()

