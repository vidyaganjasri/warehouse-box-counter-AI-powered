import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import time
import sys
from ultralytics import YOLO

# Add YOLOv8 root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# === Setup directories ===
SAVE_DIR = "saved_frames"
CAPTURE_DIR = "yolov8/captures"
DETECT_DIR = "yolov8/detect"
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(CAPTURE_DIR, exist_ok=True)
os.makedirs(DETECT_DIR, exist_ok=True)

# ======= Styled Button Class =======
class StyledButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="#2c2f33", fg="white", font=("Helvetica", 12),
                       activebackground="#40444b", activeforeground="#00ffcc",
                       relief="flat", bd=1, padx=10, pady=5, highlightthickness=0,
                       cursor="hand2")

# ======= Main Application Class =======
class WarehouseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 Warehouse Box Detection")
        self.root.geometry("1000x750")
        self.root.configure(bg="#1e1e1e")

        self.cap = None
        self.current_frame = None
        self.detected_image_path = None
        self.box_count = 0

        self._build_ui()

    def _build_ui(self):
        self.navbar_frame = tk.Frame(self.root, bg="#2c2f33", height=50)
        self.navbar_frame.pack(fill="x", side="top")

        self.menu_button = StyledButton(self.navbar_frame, text="☰ Menu", command=self.toggle_menu)
        self.menu_button.pack(side="left", padx=10, pady=10)

        self.title_label = tk.Label(self.navbar_frame, text="📦 Warehouse Box Detection",
                                    font=("Helvetica", 18, "bold"), bg="#2c2f33", fg="white")
        self.title_label.pack(pady=5)

        self.menu_panel = tk.Frame(self.root, bg="#2c2f33")
        self.menu_panel.place(x=0, y=50, relwidth=0.25, relheight=1)
        self.menu_panel_visible = False
        self._add_menu_buttons()

        self.display_area = tk.Label(self.root, bg="#111111")
        self.display_area.place(relx=0.28, rely=0.15, width=640, height=400)

        self.count_label = tk.Label(self.root, text="📦 Boxes Detected: 0", font=("Helvetica", 14),
                                    bg="#1e1e1e", fg="white")
        self.count_label.place(relx=0.4, rely=0.70)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#1e1e1e", fg="#00ffcc")
        self.status_label.place(relx=0.4, rely=0.74)

        self.control_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.control_frame.place(relx=0.3, rely=0.8, width=640, height=50)
        self.control_frame.pack_propagate(False)

        self.capture_btn = StyledButton(self.control_frame, text="📸 Capture Photo", command=self.capture_photo)
        self.capture_btn.pack(side="left", padx=10)

        self.upload_btn = StyledButton(self.control_frame, text="🖼 Upload Image", command=self.upload_image)
        self.upload_btn.pack(side="left", padx=10)

        self.detect_btn = StyledButton(self.control_frame, text="🧠 Detect Boxes", command=self.run_yolo_detection)
        self.detect_btn.pack(side="left", padx=10)

        self.save_btn = StyledButton(self.control_frame, text="💾 Save Image", command=self.save_frame)
        self.save_btn.pack(side="right", padx=10)

        self.quit_btn = StyledButton(self.control_frame, text="❌ Quit", command=self.quit_app)
        self.quit_btn.pack(side="right", padx=10)

    def _add_menu_buttons(self):
        options = [("🗂 Saved Frames", self.view_saved_frames)]
        for (text, cmd) in options:
            btn = StyledButton(self.menu_panel, text=text, command=cmd)
            btn.pack(pady=10, fill="x", padx=10)

    def toggle_menu(self):
        if self.menu_panel_visible:
            self.menu_panel.place_forget()
        else:
            self.menu_panel.place(x=0, y=50, relwidth=0.25, relheight=1)
        self.menu_panel_visible = not self.menu_panel_visible

    def _show_frame(self, frame):
        frame = cv2.resize(frame, (640, 400))
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.display_area.imgtk = img
        self.display_area.configure(image=img)

    def capture_photo(self):
        self.cap = cv2.VideoCapture(0)
        ret, frame = self.cap.read()
        self.cap.release()
        if ret:
            capture_path = os.path.join(CAPTURE_DIR, "image.jpg")
            cv2.imwrite(capture_path, frame)
            self.current_frame = frame
            self._show_frame(frame)
            self.count_label.config(text="📦 Boxes Detected: 0")
            self.status_label.config(text="📸 Photo captured and saved.")
        else:
            messagebox.showerror("Error", "Failed to capture photo from webcam.")

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not path:
            return
        img = cv2.imread(path)
        if img is None:
            messagebox.showerror("Error", "Failed to load image.")
            return
        capture_path = os.path.join(CAPTURE_DIR, "image.jpg")
        cv2.imwrite(capture_path, img)
        self.current_frame = img
        self._show_frame(img)
        self.count_label.config(text="📦 Boxes Detected: 0")
        self.status_label.config(text="🖼 Image uploaded and saved.")

    def run_yolo_detection(self):
        image_path = os.path.join(CAPTURE_DIR, "image.jpg")
        if not os.path.exists(image_path):
            messagebox.showwarning("Warning", "No image found to detect. Please capture or upload an image first.")
            return

        model = YOLO("yolov8n.pt")  # You can replace this with your custom model
        results = model(image_path)
        img = cv2.imread(image_path)
        box_count = 0

        for result in results:
            boxes = result.boxes.xyxy.cpu().numpy()
            box_count = len(boxes)
            for box in boxes:
                x1, y1, x2, y2 = map(int, box[:4])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        output_path = os.path.join(DETECT_DIR, "detected.jpg")
        cv2.imwrite(output_path, img)
        self.current_frame = img
        self.box_count = box_count
        self._show_frame(img)

        self.count_label.config(text=f"📦 Boxes Detected: {box_count}")
        self.status_label.config(text="🧠 Detection completed.")

    def save_frame(self):
        if self.current_frame is None:
            messagebox.showwarning("Warning", "No frame to save.")
            return
        filename = f"{SAVE_DIR}/frame_{int(time.time())}.jpg"
        cv2.imwrite(filename, self.current_frame)
        messagebox.showinfo("Saved", f"Frame saved as {filename}")

    def view_saved_frames(self):
        popup = Toplevel(self.root)
        popup.title("Saved Frames")
        popup.geometry("800x500")
        popup.configure(bg="#1e1e1e")
        files = sorted(os.listdir(SAVE_DIR), reverse=True)[:10]
        for i, fname in enumerate(files):
            path = os.path.join(SAVE_DIR, fname)
            img = Image.open(path).resize((160, 120))
            imgtk = ImageTk.PhotoImage(img)
            lbl = tk.Label(popup, image=imgtk, bg="#1e1e1e")
            lbl.image = imgtk
            lbl.grid(row=i // 5, column=(i % 5) * 2, padx=10, pady=10)
            del_btn = StyledButton(popup, text="❌", command=lambda p=path, w=popup: self._delete_frame(p, w))
            del_btn.grid(row=i // 5, column=(i % 5) * 2 + 1)

    def _delete_frame(self, path, win):
        if os.path.exists(path):
            os.remove(path)
            messagebox.showinfo("Deleted", f"Deleted: {os.path.basename(path)}")
            win.destroy()
            self.view_saved_frames()

    def quit_app(self):
        if self.cap and self.cap.isOpened():
            self.cap.release()
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = WarehouseApp(root)
    root.mainloop()
