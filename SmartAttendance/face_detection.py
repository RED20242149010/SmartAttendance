import cv2

MODEL_PATH = "models/face_detection_yunet_2023mar_int8.onnx"

detector = cv2.FaceDetectorYN.create(
    MODEL_PATH,
    "",
    (320, 320),
    0.9,
    0.3,
    5000
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Could not open webcam.")
    exit()

print("Face detection started.")
print("Press Q to quit.")

while True:

    ret, frame = camera.read()

    if not ret:
        print("ERROR: Could not read frame.")
        break

    height, width = frame.shape[:2]

    detector.setInputSize((width, height))

    _, faces = detector.detect(frame)

    if faces is not None:

        for face in faces:

            x = int(face[0])
            y = int(face[1])
            w = int(face[2])
            h = int(face[3])

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    cv2.imshow("Smart Attendance - Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()