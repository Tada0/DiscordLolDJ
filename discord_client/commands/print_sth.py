from discord_client.discord_client import DiscordClient
from discord.ext import commands
import logging

@commands.command(name='haloziom', pass_context=True)
async def hello(context):
    logging.getLogger('discord.custom').info("Odpowiedzialem no siema")
    await context.send(f"No siema")

async def setup(client: DiscordClient):
    client.add_command(hello)
