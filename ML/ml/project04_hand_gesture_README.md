# Project04 Hand Gesture Classifier

OpenCV webcam ROI images are collected, resized to a fixed input size, and used to train a small CNN hand gesture classifier.

This is a portfolio-scale image classification project. It is not a production object detector. The goal is to show the full workflow: data collection, preprocessing, training, feedback collection, retraining, and webcam inference.

## Classes

```text
open_hand
fist
peace
unknown
```

`unknown` means "do not classify as a supported gesture." It should contain empty ROI images, partial hands, unclear hand poses, background objects, blurred frames, and other frames that are not `open_hand`, `fist`, or `peace`.

## Files

```text
project04_hand_gesture_collect.py      # OpenCV ROI sample collector
project04_train_hand_gesture_model.py  # CNN training script
project04_hand_gesture_webcam.py       # Webcam ROI inference and feedback capture
project04_hand_gesture_utils.py        # Shared class, preprocessing, and prediction helpers
project04_realtime_utils.py            # ROI crop helpers
project04_hand_gesture_classifier.ipynb # Notebook version of the workflow
project04_hand_gesture.keras           # Latest trained model
hand_gesture_dataset/                  # Current training dataset
```

Current cleaned dataset count:

```text
open_hand: 131
fist: 222
peace: 216
unknown: 66
total: 635
```

Latest retrained model result on the cleaned local dataset:

```text
total: 617/635 = 0.972
open_hand: 129/131
fist: 217/222
peace: 206/216
unknown: 65/66
```

This number is measured on the current collected dataset, so it is useful as a development check but should not be treated as real-world accuracy.

## Setup on Another Windows PC

Run these commands from the repository root.

```powershell
py -m venv ML/.venv
ML/.venv/Scripts/python.exe -m pip install --upgrade pip
ML/.venv/Scripts/python.exe -m pip install -r ML/ml/project04_hand_gesture_requirements.txt
```

If `py` is not available, use your installed Python path instead.

## 1. Collect Samples

```powershell
ML/.venv/Scripts/python.exe ML/ml/project04_hand_gesture_collect.py --camera 0 --roi-size 320
```

Keys:

```text
1 -> open_hand
2 -> fist
3 -> peace
4 -> unknown
q / ESC -> quit
```

Recommended next target:

```text
open_hand: 200+ images
fist: 200+ images
peace: 200+ images
unknown: 200+ images with varied negative examples
```

Keep the webcam position, ROI size, lighting, and background close to the inference environment.

## 2. Train

Use the current cleaned dataset without class downsampling:

```powershell
ML/.venv/Scripts/python.exe ML/ml/project04_train_hand_gesture_model.py --epochs 30 --batch-size 16 --no-balance --no-sample-weight
```

Saved model:

```text
ML/ml/project04_hand_gesture.keras
```

If there is no model file yet, this training command creates it after the dataset folders contain images for every class.

## 3. Run Webcam Classifier

```powershell
ML/.venv/Scripts/python.exe ML/ml/project04_hand_gesture_webcam.py --camera 0 --threshold 0.50 --unknown-margin 0.15
```

During inference:

```text
s -> save current predicted ROI to hand_gesture_captures/
1 -> save ROI feedback as open_hand
2 -> save ROI feedback as fist
3 -> save ROI feedback as peace
4 -> save ROI feedback as unknown
q / ESC -> quit
```

After saving feedback images, run training again.

## Validation

```powershell
ML/.venv/Scripts/python.exe ML/tests/test_project04_hand_gesture_utils.py
ML/.venv/Scripts/python.exe -m py_compile ML/ml/project04_hand_gesture_utils.py ML/ml/project04_hand_gesture_collect.py ML/ml/project04_train_hand_gesture_model.py ML/ml/project04_hand_gesture_webcam.py
```

## Portfolio Summary

This project demonstrates a practical machine-learning loop:

1. Define a simple gesture classification problem.
2. Use OpenCV to collect ROI-based webcam images.
3. Normalize all images to the same model input size.
4. Train a CNN classifier with TensorFlow/Keras.
5. Run real-time webcam inference inside the ROI.
6. Save incorrect predictions as feedback data.
7. Clean mislabeled images and retrain.

The key learning point is that model accuracy depends more on dataset quality and representative `unknown` examples than on making the CNN architecture complicated.
