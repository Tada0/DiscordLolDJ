import logging.handlers
import logging

#TODO: put logging file location in .env, rotate through new file for each bot run, discord-1.log, discord-2.log etc. or use uuid, put info inside which run was it (timestamp or sth else)

def setup_logger():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
        mode='w'
    )

    datetime_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', datetime_format, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
