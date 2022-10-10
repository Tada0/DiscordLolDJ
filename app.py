#!/usr/bin/env python3
from discord_client.discord_client import DiscordClient
from utils.logger import setup_logger
from config.env_config import get_env
import asyncio
from riotwatcher import LolWatcher
from dal.context import DBContext

async def main():
    setup_logger()
    context = DBContext()
    async with DiscordClient() as client:
        await client.load_boot_extensions()
        await client.start(token=get_env("token"))

if __name__ == '__main__':
    asyncio.run(main())