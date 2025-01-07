from pyrogram import filters
from pyrogram.types import Message
from bot import JunctionBot
from config import Config
from ..utils.forward_message import forward_message

def forward_filter(_, __, m: Message):
    for task in Config.TASKS:
        if m.chat.id == int(task["from"]):
            return True
    return False

@JunctionBot.on_message(filters.create(forward_filter) & filters.incoming)
async def _(c: JunctionBot, m: Message):
    await forward_message(c, m)