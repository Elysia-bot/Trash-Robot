# Hướng dẫn Thiết lập

Thực hiện tuần tự các bước sau

---

## 1. Điều kiện tiên quyết: Cài đặt Python 3.12.10 (Do Thằng Cơ thích 3.12.10  ┐(￣ヘ￣;)┌  )
Dự án bắt buộc sử dụng **Python 3.12.10**. Không sử dụng các phiên bản thử nghiệm mới như Python 3.14+ để tránh lỗi xung đột môi trường và lỗi biên dịch thư viện Pygame. Chọn **một trong hai** cách cài đặt sau (Tao khuyên dùng cách B):

### Cách A: Sử dụng Bộ cài đặt Đồ họa (Thủ công)
1. Tải bộ cài đặt chính thức cho Windows: [Python 3.12.10 Windows Installer](https://www.python.org/downloads/release/python-31210/).
2. Chạy file `.exe` vừa tải về.
3. **BẮT BUỘC:** Tích chọn ô **"Add python.exe to PATH"** ở dưới cùng cửa sổ trước khi nhấn *Install Now*.

### Cách B: Sử dụng Windows Package Manager (Qua Terminal)
Mở Command Prompt (CMD) và chạy lệnh sau để cài đặt tự động:
```bash
winget install Python.Python.3.12
```
## 2. Tải Dependencies và cập nhật Pip
Dùng lệnh sau:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

## 3. Tải Datasets
Nguồn: https://universe.roboflow.com/project-g6oev/trash-s8fg7/dataset/5/download/yolov8
Lưu ý: Tại giao diện tải của Roboflow, hãy chọn tùy chọn tải về dưới dạng tệp ZIP.

## 4. Đổi tên
Đổi tên tệp mới tải về (Tên Yolo gì ấy) thành "datasets" (Do Thằng Cơ để đoạn mã train tìm thư mục có tên "datasets"  ┐(￣～￣)┌ )

## 5. Cấu hình tải
Trường hợp máy tính cấu hình yếu: Điều chỉnh cấu hình epoch về 8 và kích thước hình ảnh (imgsz) về 320
Trường hợp máy tính có GPU rời: Cấu hình tham số thiết bị (device) chuyển sang sử dụng GPU thay vì mặc định chạy bằng CPU