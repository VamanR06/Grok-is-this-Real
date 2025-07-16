import os
from bot import Bot
from utils import *
from constants import TOKEN

os.chdir("./")

disc_bot = Bot()
disc_bot.initialize(TOKEN)