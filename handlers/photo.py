import os
import time

from config import DOWNLOAD_DIR, OUTPUT_DIR
from utils.storage import (
    set_source,
    get_source,
    clear_source
)

from utils.faceswap import swap_faces

def register(bot):

    @bot.message_handler(content_types=["photo"])
    def photo_handler(message):

        user_id = message.from_user.id

        file_info = bot.get_file(
            message.photo[-1].file_id
        )

        file_data = bot.download_file(
            file_info.file_path
        )

        photo_path = os.path.join(
            DOWNLOAD_DIR,
            f"{user_id}_{int(time.time())}.jpg"
        )

        with open(photo_path, "wb") as f:
            f.write(file_data)

        source = get_source(user_id)

        if source is None:

            set_source(user_id, photo_path)

            bot.reply_to(
                message,
                "✅ Đã lưu ảnh nguồn.\nGửi ảnh đích để ghép mặt."
            )

            return

        output_path = os.path.join(
            OUTPUT_DIR,
            f"swap_{user_id}.jpg"
        )

        try:

            swap_faces(
                source,
                photo_path,
                output_path
            )

            with open(output_path, "rb") as img:
                bot.send_photo(
                    message.chat.id,
                    img,
                    caption="✅ Ghép mặt hoàn tất"
                )

        except Exception as e:

            bot.reply_to(
                message,
                f"❌ Lỗi: {str(e)}"
            )

        finally:

            clear_source(user_id)
