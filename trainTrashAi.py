from ultralytics import YOLO

def main():
    # 1. Tải mô hình YOLOv11 phiên bản Nano (nhẹ nhất cho CPU)
    model = YOLO("yolo11n.pt") 

    # 2. Bắt đầu huấn luyện (Fine-tuning)
    model.train(
        data="datasets/data.yaml", # Đường dẫn cực kỳ gọn sạch
        epochs=10,
        imgsz=640,
        device="cpu"
    )

if __name__ == '__main__':
    main()