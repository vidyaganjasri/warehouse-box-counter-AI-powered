import os
import yaml
import glob
import tensorflow as tf
import keras_cv
from matplotlib import pyplot as plt

# --- 1. Configuration ---
MODEL_PATH = "retinanet_best.keras"
BOUNDING_BOX_FORMAT = "rel_xywh"

with open("warehouse-dataset/data.yaml", 'r') as f:
    data_yaml = yaml.safe_load(f)
CLASS_MAPPING = {i: name for i, name in enumerate(data_yaml['names'])}
TEST_IMAGE_DIR = data_yaml['test']

try:
    IMAGE_PATH = glob.glob(os.path.join(TEST_IMAGE_DIR, "*.jpg"))[0]
except IndexError:
    print(f"Error: No .jpg images found in the test directory: {TEST_IMAGE_DIR}")
    exit()

# --- 2. Load Model & Predict ---
model = tf.keras.models.load_model(MODEL_PATH, custom_objects=keras_cv.models.RetinaNet.custom_objects)

image = tf.io.read_file(IMAGE_PATH)
image = tf.image.decode_jpeg(image)
image_resized = tf.image.resize(image, (640, 640))
image_batch = tf.expand_dims(image_resized, axis=0)

y_pred = model.predict(image_batch)

# --- 3. Visualize the Results ---
keras_cv.visualization.plot_bounding_box_gallery(
    image_batch, value_range=(0, 255), rows=1, cols=1,
    y_pred=y_pred,
    scale=5, font_scale=0.7,
    bounding_box_format=BOUNDING_BOX_FORMAT,
    class_mapping=CLASS_MAPPING,
    show=True
)
plt.show() # Make sure the plot is displayed