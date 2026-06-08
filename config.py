import os

# Telegram Bot Token
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError(
        "Không tìm thấy BOT_TOKEN. Hãy đặt biến môi trường BOT_TOKEN."
    )

# Thư mục lưu ảnh
DOWNLOAD_DIR = "downloads"
OUTPUT_DIR = "outputs"

# Tạo thư mục nếu chưa tồn tại
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Tên model Face Swap
FACE_MODEL = "buffalo_l"
SWAP_MODEL = "inswapper_128.onnx"

# CPU = 0, GPU NVIDIA = 1 (nếu có CUDA)
USE_GPU = False
