import os
from config import Config
from bot import JunctionBot
from pyrogram import filters
from pyrogram.types import Message
from bot.utils.forward_message import forward_message
import bot.plugins.settings
import bot.plugins.get_chats

# Создаем рабочую директорию, если она не существует
if not os.path.exists(Config.WORK_DIR):
    os.makedirs(Config.WORK_DIR)

# Инициализация бота
config = Config()
bot = JunctionBot(config)

# Определение фильтра для пересылки сообщений
def forward_filter(_, __, m: Message):
    for task in Config.TASKS:
        if m.chat.id == int(task["from"]):
            return True
    return False

# Обработчик сообщений для пересылки
@bot.on_message(filters.create(forward_filter) & filters.incoming)
async def handler(client, message):
    await forward_message(client, message)

# Запуск бота
if __name__ == "__main__":
    bot.run()