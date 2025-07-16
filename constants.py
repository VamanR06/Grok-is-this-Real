from dotenv import load_dotenv
from os import environ

load_dotenv()

TOKEN = environ.get("TOKEN")

XAI_API_KEY = environ.get("XAI_API_KEY")
XAI_BASE_URL = "https://api.x.ai/v1"
XAI_MODEL = "gpt-4.1-nano"

COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "default": "\033[37m",
}

OWNER_IDS = [587711023658827787, 617892283949383681]

COLOR_MAIN = 0xCEB512
COLOR_GOOD = 0x0AE636
COLOR_NEUTRAL = 0xD9DD0E
COLOR_BAD = 0xF00000