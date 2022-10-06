from typing import Mapping
from dotenv import dotenv_values
from pathlib import Path
import sys

def __read_env() -> Mapping[str, str]:
    dotenv_path = Path(".") / '.env'
    return dotenv_values(dotenv_path=dotenv_path)

def get_env(key: str) -> str:
    try:
        return __read_env()[key]
    except KeyError as error:
        print(error)
        sys.exit(1)