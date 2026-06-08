import telebot

from config import BOT_TOKEN

from handlers.start import register as start_register
from handlers.photo import register as photo_register

bot = telebot.TeleBot(BOT_TOKEN)

start_register(bot)
photo_register(bot)

print("Bot đang chạy...")

bot.infinity_polling(
    skip_pending=True
)
