from discord_client.discord_client import DiscordClient
from utils.logger import setup_logger
from config.env_config import get_env
import asyncio

async def main():
    setup_logger()
    async with DiscordClient() as client:
        await client.load_extensions()
        await client.start(token=get_env("token"))

if __name__ == '__main__':
    asyncio.run(main())