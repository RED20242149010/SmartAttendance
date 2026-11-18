
import cv2
import os
import csv
import re
import requests
from datetime import datetime
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DETECTOR_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "face_detection_yunet_2023mar_int8.onnx"
)

RECOGNITION_MODEL = os.path.join(
    BASE_DIR,
    "models",
    "face_recognition_sface_2021dec_int8.onnx"
)

FACES_FOLDER = os.path.join(BASE_DIR, "faces")
ATTENDANCE_FILE = os.path.join(BASE_DIR, "attendance.csv")

DJANGO_URL = "http://127.0.0.1:8000/api/mark-attendance/"

MATCH_THRESHOLD = 0.45
MIN_SCORE_GAP = 0.05

if not os.path.exists(DETECTOR_MODEL):
    print("ERROR: Face detection model not found:", DETECTOR_MODEL)
    exit()

if not os.path.exists(RECOGNITION_MODEL):
    print("ERROR: Face recognition model not found:", RECOGNITION_MODEL)
    exit()

if not os.path.isdir(FACES_FOLDER):
    print("ERROR: Faces folder not found:", FACES_FOLDER)
    exit()

detector = cv2.FaceDetectorYN.create(
    DETECTOR_MODEL,
    "",
    (320, 320),
    0.5,
    0.3,
    5000
)

recognizer = cv2.FaceRecognizerSF.create(
    RECOGNITION_MODEL,
    ""
)

known_faces = defaultdict(list)

print("Loading registered faces...")

for filename in os.listdir(FACES_FOLDER):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    path = os.path.join(FACES_FOLDER, filename)
    image = cv2.imread(path)

    if image is None:
        print("Could not load:", filename)
        continue

    height, width = image.shape[:2]

    detector.setInputSize((width, height))

    _, faces = detector.detect(image)

    if faces is None or len(faces) == 0:
        print("No face found in:", filename)
        continue

    face = max(faces, key=lambda f: f[2] * f[3])

    aligned_face = recognizer.alignCrop(image, face)
    feature = recognizer.feature(aligned_face)

    name = os.path.splitext(filename)[0]
    name = re.sub(r"_\d+$", "", name)

    known_faces[name].append(feature)

    print("Loaded:", filename, "as", name)


if len(known_faces) == 0:
    print("ERROR: No registered faces found.")
    exit()


print("\nRegistered people:")

for name, features in known_faces.items():
    print("-", name, "(", len(features), "photos )")


attendance_today = set()

if os.path.exists(ATTENDANCE_FILE):

    with open(
        ATTENDANCE_FILE,
        "r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        today = datetime.now().strftime("%Y-%m-%d")

        for row in reader:

            if row.get("Date") == today:
                attendance_today.add(row.get("Name"))


django_sent_today = set()


def mark_attendance(name):

    now = datetime.now()

    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    if name not in attendance_today:

        file_exists = os.path.exists(ATTENDANCE_FILE)

        try:

            with open(
                ATTENDANCE_FILE,
                "a",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                writer = csv.writer(file)

                if (
                    not file_exists
                    or os.path.getsize(ATTENDANCE_FILE) == 0
                ):
                    writer.writerow(["Name", "Date", "Time"])

                writer.writerow([
                    name,
                    today,
                    current_time
                ])

            attendance_today.add(name)

            print("CSV attendance marked:", name)
            print("CSV saved at:", ATTENDANCE_FILE)

        except OSError as e:

            print("CSV saving error:", e)


    if name in django_sent_today:
        return

    try:

        response = requests.post(
            DJANGO_URL,
            json={"name": name},
            timeout=5
        )

        if response.status_code == 200:

            data = response.json()

            print("Django:", data.get("message"))

            django_sent_today.add(name)

        else:

            print("Django error:", response.status_code)
            print(response.text)

    except requests.exceptions.RequestException as e:

        print("Could not connect to Django:", e)


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open webcam.")
    exit()


print("\nFace recognition started.")
print("Django attendance API ready.")
print("CSV attendance file:", ATTENDANCE_FILE)
print("Press Q to quit.")


while True:

    ret, frame = camera.read()

    if not ret:
        print("ERROR: Could not read webcam.")
        break

    height, width = frame.shape[:2]

    detector.setInputSize((width, height))

    _, faces = detector.detect(frame)

    if faces is not None:

        for face in faces:

            aligned_face = recognizer.alignCrop(frame, face)
            feature = recognizer.feature(aligned_face)

            person_scores = []

            for name, registered_features in known_faces.items():

                best_person_score = max(
                    float(
                        recognizer.match(
                            known_feature,
                            feature,
                            cv2.FaceRecognizerSF_FR_COSINE
                        )
                    )
                    for known_feature in registered_features
                )

                person_scores.append(
                    (name, best_person_score)
                )

            person_scores.sort(
                key=lambda item: item[1],
                reverse=True
            )

            best_name = "Unknown"
            best_score = person_scores[0][1]

            if best_score >= MATCH_THRESHOLD:

                if len(person_scores) == 1:

                    best_name = person_scores[0][0]

                else:

                    second_score = person_scores[1][1]

                    if best_score - second_score >= MIN_SCORE_GAP:
                        best_name = person_scores[0][0]

            x = int(face[0])
            y = int(face[1])
            w = int(face[2])
            h = int(face[3])

            if best_name != "Unknown":

                label = f"{best_name} - {best_score:.2f}"
                color = (0, 255, 0)

                mark_attendance(best_name)

            else:

                label = f"Unknown - {best_score:.2f}"
                color = (0, 0, 255)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                color,
                2
            )

            cv2.putText(
                frame,
                label,
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

    cv2.imshow(
        "Smart Attendance - Face Recognition",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()

print("Face recognition stopped.")
