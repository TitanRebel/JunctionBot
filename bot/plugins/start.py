from pyrogram import filters
from pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from bot import JunctionBot

@JunctionBot.on_message(filters.command("start") & filters.incoming & filters.private)
async def start(c: JunctionBot, m: Message):
    # Создаем клавиатуру с командами
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("/add_task")],
            [KeyboardButton("/del_task")],
            [KeyboardButton("/list_tasks")],
            [KeyboardButton("/get_chats")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

    await m.reply_text(
        "Привет, это бот для пересылки сообщений. Я могу пересылать сообщения из одного чата в другой.\n\nКоманды которые вы можете использовать появились у вас в клавиатуре",
        reply_markup=keyboard,
        reply_to_message_id=m.id
    )

# Обработчики команд (опционально)
@JunctionBot.on_message(filters.command("add_task") & filters.incoming & filters.private)
async def add_task_handler(c: JunctionBot, m: Message):
    await m.reply_text("Для добавления задачи, используйте: /add_task <group_from_id> <group_to_id>")

@JunctionBot.on_message(filters.command("del_task") & filters.incoming & filters.private)
async def del_task_handler(c: JunctionBot, m: Message):
    await m.reply_text("To delete a task, use the command: /del_task <task_id>")

@JunctionBot.on_message(filters.command("list_tasks") & filters.incoming & filters.private)
async def list_tasks_handler(c: JunctionBot, m: Message):
    await m.reply_text("To list all tasks, use the command: /list_tasks")