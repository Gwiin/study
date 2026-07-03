# Project04: OpenCV ROI Hand Gesture Classifier

## Project Goal

Build a simple portfolio project that classifies hand gestures from a webcam ROI using image classification.

The first idea was real-time person/animal/unknown classification, but live object recognition was not stable enough for the available dataset. The project direction was narrowed to a more suitable scope: fixed ROI hand gesture classification with OpenCV and a CNN model.

## Problem Definition

The webcam frame contains a centered ROI. The model classifies only the ROI image into one of four classes:

```text
open_hand
fist
peace
unknown
```

`unknown` is used when the ROI does not contain one of the supported gestures.

## Workflow

1. Collect ROI images with OpenCV.
2. Store images in class folders.
3. Resize images to `128 x 128`.
4. Convert BGR images to RGB.
5. Normalize pixel values to `0.0 - 1.0`.
6. Train a CNN classifier with TensorFlow/Keras.
7. Run webcam inference on the same ROI.
8. Save wrong predictions as feedback data.
9. Move mislabeled samples to the correct class.
10. Retrain and compare model performance.

## Dataset

Current cleaned dataset:

```text
open_hand: 131
fist: 222
peace: 216
unknown: 66
total: 635
```

The dataset is intentionally small because this is a portfolio-scale project. The next improvement target is to increase `unknown` and collect more varied webcam conditions.

## Model

The model is a small CNN:

```text
input: 128 x 128 x 3
RandomFlip
RandomRotation
RandomZoom
Conv2D + MaxPooling
Conv2D + MaxPooling
Conv2D + MaxPooling
Flatten
Dropout
Dense
Softmax output
```

The model file is saved as:

```text
ML/ml/project04_hand_gesture.keras
```

## Retraining Result

Before cleaning and retraining, the default model scored:

```text
603/635 = 95.0%
```

After removing clear mislabels and retraining:

```text
617/635 = 97.2%
```

Class result:

```text
open_hand: 129/131
fist: 217/222
peace: 206/216
unknown: 65/66
```

This evaluation is based on the current collected dataset. It is not a guarantee of real-world accuracy.

## What This Project Shows

- OpenCV webcam control
- ROI extraction from live video
- Image dataset collection
- Label feedback loop
- CNN image classification
- Model retraining after data cleaning
- Basic validation with tests
- Practical limitation analysis

## Limitations

- The dataset is still small.
- `unknown` examples are not diverse enough.
- Performance can change with lighting, camera angle, background, hand distance, and ROI placement.
- This is classification inside a fixed ROI, not full object detection.

## Next Improvements

- Increase every class to at least 200 images.
- Increase `unknown` with empty backgrounds, objects, partial hands, blurred frames, and unclear poses.
- Collect samples under different lighting and camera distances.
- Keep a separate test dataset that is never used for training.
- Add a confusion matrix report after each training run.
- Consider MediaPipe hand landmark extraction if image-only classification becomes unstable.
