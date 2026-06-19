import pygame
from detector import detect_trash
from robot import Robot

pygame.init()

IMAGE_PATH = "environment.jpg"

# img = pygame.image.load(IMAGE_PATH)

# img_w = img.get_width()
# img_h = img.get_height()

# screen = pygame.display.set_mode(
#     (img_w, img_h + 100)
# )

# Load ảnh gốc
img_original = pygame.image.load(IMAGE_PATH)
orig_w = img_original.get_width()
orig_h = img_original.get_height()

# Đặt chiều rộng mong muốn cho vừa màn hình máy tính (ví dụ: 1024)
TARGET_W = 1024
# Tính toán chiều cao theo tỷ lệ ảnh gốc để không bị méo hình
scale_ratio = TARGET_W / orig_w
TARGET_H = int(orig_h * scale_ratio)

# Thu nhỏ bức ảnh lại
img = pygame.transform.smoothscale(img_original, (TARGET_W, TARGET_H))
img_w = TARGET_W
img_h = TARGET_H

# Tạo màn hình theo kích thước mới (vẫn cộng thêm 100 để hiện text bên dưới)
screen = pygame.display.set_mode((img_w, img_h + 100))

pygame.display.set_caption(
    "EcoGuardian AI"
)

font = pygame.font.SysFont(None, 30)

robot = Robot()

detections = detect_trash(IMAGE_PATH)

# target = None

# if len(detections) > 0:

#     target = detections[0]

#     robot.state = "MOVING"

# Tạo một danh sách các bãi rác cần dọn
targets_list = list(detections)  # Lưu lại tất cả các node rác tìm thấy
target = None

if len(targets_list) > 0:
    # Lấy mục tiêu đầu tiên ra khỏi danh sách để đi dọn
    target = targets_list.pop(0)
    robot.state = "MOVING"

clock = pygame.time.Clock()

collected = False

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # if target and not collected:

    #     tx, ty = target["center"]

    #     #arrived = robot.move_to(tx, ty)
    #     arrived = robot.move_to(tx * scale_ratio, ty * scale_ratio)

    #     if arrived:

    #         robot.state = "COLLECTED"

    #         robot.collected += 1

    #         collected = True

    # Nếu có mục tiêu hiện tại
    if target:
        tx, ty = target["center"]
        arrived = robot.move_to(tx * scale_ratio, ty * scale_ratio)

        if arrived:
            robot.collected += 1
            
            # Kiểm tra xem còn rác trong danh sách không
            if len(targets_list) > 0:
                # Nếu còn rác, lấy mục tiêu tiếp theo ra để đi dọn tiếp!
                target = targets_list.pop(0)
                robot.state = "MOVING"
            else:
                # Nếu đã dọn sạch sành sanh không còn node nào
                target = None
                robot.state = "ALL COLLECTED"
                collected = True

    screen.fill((255,255,255))

    screen.blit(img, (0,0))

    if target: #and not collected:

        x1,y1,x2,y2 = target["box"]

        pygame.draw.rect(
            screen,
            (0,255,0),
            pygame.Rect(
                int(x1),
                int(y1),
                int(x2-x1),
                int(y2-y1)
            ),
            3
        )

    pygame.draw.circle(
        screen,
        (0,100,255),
        (int(robot.x), int(robot.y)),
        15
    )

    state_text = font.render(
        f"State: {robot.state}",
        True,
        (0,0,0)
    )

    collect_text = font.render(
        f"Collected: {robot.collected}",
        True,
        (0,0,0)
    )

    screen.blit(state_text, (20, img_h + 10))
    screen.blit(collect_text, (20, img_h + 40))

    if collected:

        done = font.render(
            "TRASH COLLECTED",
            True,
            (255,0,0)
        )

        screen.blit(done, (250, img_h + 20))

    pygame.display.flip()

pygame.quit()