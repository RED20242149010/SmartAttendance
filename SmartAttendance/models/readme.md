# Face Recognition Models

## Overview

This folder contains the pre-trained deep learning models used in the Smart Attendance Management System.

The system uses two OpenCV-compatible ONNX models for face detection and face recognition.

## Model Files

### 1. YuNet – Face Detection

**Filename:**
`face_detection_yunet_2023mar_int8.onnx`

**Purpose:**

- Detects human faces from webcam frames.
- Identifies face locations.
- Provides facial landmarks for face alignment.
- Supports real-time face detection.

**Used in:** `face_recognition.py` and `face_detection.py`

### 2. SFace – Face Recognition

**Filename:**
`face_recognition_sface_2021dec_int8.onnx`

**Purpose:**

- Extracts facial features from detected faces.
- Generates face feature representations.
- Compares live faces with registered student faces.
- Helps identify registered students.

**Used in:** `face_recognition.py`

## Folder Structure

```text
models/
│
├── face_detection_yunet_2023mar_int8.onnx
├── face_recognition_sface_2021dec_int8.onnx
└── README.md
```

## Technologies

- OpenCV
- YuNet Face Detection
- SFace Face Recognition
- ONNX (Open Neural Network Exchange)

## Working Process

1. The webcam captures a live image.
2. The YuNet model detects faces.
3. The detected faces are aligned.
4. The SFace model extracts facial features.
5. Extracted features are compared with registered student features.
6. The system identifies the matching student when the recognition criteria are met.

## Important Notes

- Keep both ONNX model files inside this `models` folder.
- Do not rename the model files because the Python scripts use their filenames.
- Make sure the model paths in the Python code are correct.
- These are pre-trained models used by the face recognition software.

## Project Module

**Project:** Smart Attendance Management System

**Folder:** models

**Purpose:** Face detection and face recognition using deep learning models.
