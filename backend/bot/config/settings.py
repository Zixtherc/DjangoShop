import os

from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
env_path = BASE_DIR.parent / '.env'
load_dotenv(dotenv_path=env_path)
TOKEN = os.getenv('TOKEN_BOT')
if not TOKEN:
    raise ValueError('Some problem with Bot Token')