from re import L
from discord.ext.commands import Bot
from discord import Intents
from typing import Any
import os

class DiscordClient(Bot):
    def __init__(self, **options: Any) -> None:
        intents = Intents.default()
        intents.message_content = True
        super().__init__(intents=intents, command_prefix=("/",), **options)

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def load_extensions(self):
        for filename in os.listdir("./discord_client/commands"):
            if filename.endswith('.py') and not filename.startswith('__init__'):
                await self.load_extension(f"discord_client.commands.{filename.split('.py')[0]}")
