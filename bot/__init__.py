from pyrogram import Client, __version__

class JunctionBot(Client):
    def __init__(self, config):
        super().__init__(
            "my_bot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            workers=config.WORKERS,
            plugins=dict(root="bot/plugins"),
            workdir=config.WORK_DIR
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"{me.first_name} started on @{me.username}.")

    async def stop(self, *args):
        me = await self.get_me()
        await super().stop()
        print(f"@{me.username} stopped. Bye.")