import pygame

# 1. Khởi tạo cấu hình cấu trúc ô
TILE_SIZE = 64  # Kích thước mỗi ô vuông (pixels)
WIDTH, HEIGHT = 10 * TILE_SIZE, 10 * TILE_SIZE

pygame.init()
surface = pygame.Surface((WIDTH, HEIGHT))

# 2. Ma trận nền tĩnh (Vị trí thực thể động được thay thế bằng nền đất/cỏ tương ứng)
STATIC_MAP = [
    [4, 4, 0, 0, 2, 2, 2, 3, 3, 3],  
    [4, 0, 0, 0, 2, 2, 2, 2, 2, 3],  # Robot(6) ở đất bằng(0), Rác(5) ở cỏ(2)
    [0, 0, 1, 1, 0, 0, 4, 4, 0, 0],  
    [2, 2, 1, 1, 0, 0, 4, 0, 0, 0],  
    [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],  # Người(7) ở đất bằng(0)
    [3, 0, 0, 4, 4, 0, 1, 1, 0, 0],  
    [2, 2, 0, 4, 4, 0, 1, 1, 2, 2],  
    [2, 2, 0, 0, 0, 0, 0, 0, 2, 2],  
    [0, 0, 3, 3, 0, 0, 0, 0, 0, 0],  
    [0, 0, 3, 3, 0, 0, 0, 0, 0, 0]   
]

# 3. Định nghĩa bảng màu RGB chuẩn theo bộ luật của bạn
COLORS = {
    0: (115, 74, 45),    # Nâu đậm
    1: (186, 140, 99),   # Nâu nhạt
    2: (144, 210, 109),  # Xanh nhạt
    3: (34, 102, 51),    # Xanh đậm
    4: (128, 128, 128)   # Xám
}

# 4. Vòng lặp vẽ lưới địa hình
for row in range(10):
    for col in range(10):
        tile_type = STATIC_MAP[row][col]
        color = COLORS[tile_type]
        
        rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(surface, color, rect)
        
        # Vẽ viền lưới màu trắng mỏng giống như hình nền mẫu của bạn
        pygame.draw.rect(surface, (245, 245, 245), rect, 1)

# 5. Xuất tệp tin hình ảnh tĩnh
pygame.image.save(surface, "environment.jpg")
print("Đã tạo thành công file environment.jpg chuẩn 10x10 tilemap!")
pygame.quit()