from ultralytics import YOLO

# 1. Load model của bạn (dùng đường dẫn tuyệt đối cho chắc)
model = YOLO(r"C:\code\trainTrashAi\runs\detect\train2\weights\best.pt")

# 2. Chạy nhận diện trên file ảnh đã tải về máy
# Thêm stream=False để ép nó không đợi camera
results = model.predict(
    source="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlRuT-E4ygTv3_ozId85NBKFZ2a-gqzMliLg&s", 
    save=True, 
    show=True, 
    conf=0.25,
    stream=False 
)

print("Đã xong! Bạn vào thư mục runs/detect/predict để xem ảnh nhé!")