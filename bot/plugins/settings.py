from pyrogram import Client, filters
from pyrogram.types import Message
from config import Config
from bot import JunctionBot

# Проверка авторизованного пользователя
def is_authorized_user(_, __, m: Message):
    return m.from_user.id == Config.AUTHORIZED_USER_ID

# Команда для добавления задачи
@JunctionBot.on_message(filters.command("add_task") & filters.create(is_authorized_user))
async def add_task(client, message: Message):
    try:
        # Разделяем сообщение на части
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            await message.reply_text("Использование: /add_task <группа_откуда> <группа_куда>")
            return
        
        group_from = parts[1]
        group_to = parts[2]

        # Создаем задачу с уникальным ID
        task_id = Config.generate_task_id()
        task = {"id": task_id, "from": group_from, "to": group_to}
        Config.TASKS.append(task)
        Config.save_tasks()  # Сохраняем задачи в файл
        
        await message.reply_text(f"Задача добавлена: ID: {task_id}, Откуда: {group_from}, Куда: {group_to}")
    except Exception as e:
        await message.reply_text(f"Произошла ошибка: {e}")

# Команда для удаления задачи
@JunctionBot.on_message(filters.command("del_task") & filters.create(is_authorized_user))
async def delete_task(client, message: Message):
    try:
        # Разделяем сообщение на части
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            await message.reply_text("Использование: /del_task <id>")
            return
        
        task_id = parts[1]
        task_index = next((index for (index, d) in enumerate(Config.TASKS) if d.get("id") == task_id), None)
        
        if task_index is None:
            await message.reply_text(f"Задача с ID {task_id} не найдена.")
        else:
            del Config.TASKS[task_index]
            Config.save_tasks()  # Сохраняем задачи в файл
            await message.reply_text(f"Задача с ID {task_id} удалена.")
    except Exception as e:
        await message.reply_text(f"Произошла ошибка: {e}")

# Команда для просмотра всех задач
@JunctionBot.on_message(filters.command("list_tasks") & filters.create(is_authorized_user))
async def list_tasks(client, message: Message):
    if not Config.TASKS:
        await message.reply_text("Нет задач.")
    else:
        tasks_list = "\n".join([f"ID: {task.get('id', 'Нет ID')}\nОткуда: {task['from']}\nКуда: {task['to']}\n" for task in Config.TASKS])
        await message.reply_text(f"Задачи:\n{tasks_list}")