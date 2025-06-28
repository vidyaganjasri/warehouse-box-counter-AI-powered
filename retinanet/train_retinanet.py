# --- train_retinanet.py ---
# --- FINAL VERSION v13 - The Correct Data Type Fix ---
import os
import yaml
import glob
import numpy as np
import tensorflow as tf
from tensorflow import keras
import keras_cv

# --- 1. Configuration ---
with open("warehouse-dataset/data.yaml", 'r') as f:
    data_yaml = yaml.safe_load(f)

CLASS_MAPPING = {i: name for i, name in enumerate(data_yaml['names'])}
NUM_CLASSES = data_yaml['nc']
BATCH_SIZE = 4
EPOCHS = 60
LEARNING_RATE = 0.0001
BOUNDING_BOX_FORMAT = "rel_xywh"

# --- 2. Model Building (Must be done first) ---
print("Building model...")
model = keras_cv.models.RetinaNet.from_preset(
    "retinanet_resnet50_pascalvoc",
    num_classes=NUM_CLASSES,
    bounding_box_format=BOUNDING_BOX_FORMAT,
)

# --- 3. Load ALL data into memory ---
def load_all_data(image_paths):
    images, bounding_boxes = [], []
    for image_path in image_paths:
        # Load image
        img = tf.io.read_file(image_path)
        img = tf.image.decode_jpeg(img, channels=3)
        images.append(img)
        
        # Load labels
        label_path = image_path.replace("images", "labels").replace(".jpg", ".txt")
        boxes, classes = [], []
        if os.path.exists(label_path):
            with open(label_path, 'r') as f:
                for line in f.readlines():
                    parts = line.strip().split()
                    if len(parts) == 5:
                        classes.append(int(parts[0]))
                        boxes.append([float(p) for p in parts[1:]])
        
        # THIS IS THE CRITICAL FIX: Convert NumPy arrays to Tensors immediately.
        bounding_boxes.append({
            "boxes": tf.constant(boxes, dtype=tf.float32),
            "classes": tf.constant(classes, dtype=tf.int32)
        })
    
    return images, bounding_boxes

print("Loading all data into memory...")
train_image_paths = glob.glob(os.path.join(data_yaml['train'], "*.jpg"))
val_image_paths = glob.glob(os.path.join(data_yaml['val'], "*.jpg"))

train_images, train_boxes = load_all_data(train_image_paths)
val_images, val_boxes = load_all_data(val_image_paths)

print(f"Loaded {len(train_images)} training and {len(val_images)} validation images.")


# --- 4. Preprocess data in memory ---
print("Preprocessing data...")
augmenter = keras_cv.layers.Augmenter(
    layers=[
        keras_cv.layers.RandomFlip(mode="horizontal", bounding_box_format=BOUNDING_BOX_FORMAT),
        keras_cv.layers.JitteredResize(
            target_size=(640, 640), scale_factor=(0.8, 1.25), bounding_box_format=BOUNDING_BOX_FORMAT),
    ]
)
resizing = keras_cv.layers.Resizing(height=640, width=640, pad_to_aspect_ratio=True, bounding_box_format=BOUNDING_BOX_FORMAT)

# --- Augment and encode training data ---
x_train, y_train_boxes = [], []
for img, box_dict in zip(train_images, train_boxes):
    augmented = augmenter({"images": img, "bounding_boxes": box_dict})
    x_train.append(augmented["images"])
    y_train_boxes.append(augmented["bounding_boxes"])

x_train = tf.convert_to_tensor(x_train)
y_train = model.label_encoder.encode_y(y_train_boxes)


# --- Resize and encode validation data ---
x_val, y_val_boxes = [], []
for img, box_dict in zip(val_images, val_boxes):
    resized = resizing({"images": img, "bounding_boxes": box_dict})
    x_val.append(resized["images"])
    y_val_boxes.append(resized["bounding_boxes"])

x_val = tf.convert_to_tensor(x_val)
y_val = model.label_encoder.encode_y(y_val_boxes)


# --- 5. Compile and Train ---
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
    classification_loss="focal",
    box_loss="smoothl1",
)

callbacks = [
    keras.callbacks.ModelCheckpoint("retinanet_best.keras", monitor="val_loss", save_best_only=True)
]

print("Starting training...")
model.fit(
    x=x_train,
    y=y_train,
    validation_data=(x_val, y_val),
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    callbacks=callbacks,
)
print("Training finished. Best model saved as retinanet_best.keras")