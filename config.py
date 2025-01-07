import os
import json
import uuid
from login import *

class Config:
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    SESSION_NAME = SESSION_NAME
    WORKERS = WORKERS
    WORK_DIR = WORK_DIR
    AUTHORIZED_USER_ID = AUTHORIZED_USER_ID
    PHONE_NUMBER = PHONE_NUMBER
    
    TASKS_FILE = os.path.join(WORK_DIR, "tasks.json")
    TASKS = []

    @staticmethod
    def load_tasks():
        if os.path.exists(Config.TASKS_FILE):
            with open(Config.TASKS_FILE, "r", encoding="utf-8") as file:
                Config.TASKS = json.load(file)
        else:
            Config.TASKS = []

    @staticmethod
    def save_tasks():
        with open(Config.TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump(Config.TASKS, file, ensure_ascii=False, indent=4)

    @staticmethod
    def generate_task_id():
        return str(uuid.uuid4())

# Загружаем задачи при запуске
Config.load_tasks()