from pyrogram import Client, filters

# Замените "my_bot" на любое имя вашего приложения
app = Client("my_bot",
             api_id=25084384,  # Ваш API ID от Telegram
             api_hash="47139e2db5de5632d2eb9252bc943efe",  # Ваш API Hash от Telegram
             bot_token="7917776402:AAFNre0bVW5nwYcK_oRvJshNAmIJssle0OI")  # Токен вашего бота

@app.on_message(filters.text)
def handle_message(client, message):
    chat_title = message.chat.title if message.chat.title else "Личный чат"
    chat_id = message.chat.id
    print(f"Сообщение отправлено в чат: {chat_title} (ID: {chat_id})")

app.run()