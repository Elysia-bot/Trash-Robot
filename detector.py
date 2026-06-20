from ultralytics import YOLO

MODEL_PATH = "runs/detect/train-4/weights/best.pt"

model = YOLO(MODEL_PATH)


def detect_trash(image_path):

    results = model(image_path, conf=0.1)

    detections = []

    for r in results:

        for box in r.boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            detections.append({
                "center": (cx, cy),
                "box": (x1, y1, x2, y2)
            })

    return detections