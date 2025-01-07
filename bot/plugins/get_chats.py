from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from bot import JunctionBot
import re

# Инициализация пользовательского клиента с использованием сохраненной сессии
user_client = Client(
    "user_session",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Проверка авторизованного пользователя
def is_authorized_user(_, __, m: Message):
    return m.from_user.id == Config.AUTHORIZED_USER_ID

# Команда для получения всех чатов
@JunctionBot.on_message(filters.command("get_chats") & filters.create(is_authorized_user))
async def get_chats(client, message):
    # Получаем последние 15 диалогов
    dialogs = [dialog async for dialog in user_client.get_dialogs(limit=10)]
    
    # Добавим отладочную информацию
    chat_list = []
    for dialog in dialogs:
        chat_info = f"ID: {dialog.chat.id}, Title: {dialog.chat.title or 'None'}, Type: {dialog.chat.type}"
        chat_list.append(chat_info)

    chat_list_str = "\n".join([re.sub(r", Type.*$", "", i) for i in chat_list if "GROUP" in i])


    await message.reply_text(f"Груповые чаты, в которых состоит пользователь:\n{chat_list_str}")

# Запуск пользовательского клиента
user_client.start()