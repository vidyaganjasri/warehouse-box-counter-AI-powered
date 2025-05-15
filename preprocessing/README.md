# 📦 Warehouse Box Detection - Preprocessing

This repository contains the *Preprocessing step* for Task 3 of the Warehouse Box Detection project. It involves processing an image to detect rectangular boxes (such as cardboard boxes) using computer vision techniques with OpenCV.

---

## ✅ Preprocessing Steps

1. *Read image from file*
2. *Convert to grayscale*
3. *Apply Gaussian Blur to remove noise*
4. *Perform edge detection (Canny)*
5. *Find and filter contours based on shape (rectangular) and size*
6. *Draw bounding boxes and count detected boxes*
7. *Display results using OpenCV windows*

---

## ⚙ Requirements

- Python 3.6 or higher
- OpenCV
```bash
pip install opencv-python
