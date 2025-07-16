import nextcord, os
from nextcord.ext import commands
from utils import color_message


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="grok!", intents=nextcord.Intents.all())
        self.unloaded_cogs = []

    def initialize(self, token: str):
        os.system("clear")
        print(
            color_message(
                message="""
  ________              __     __________              .___________ 
 /  _____/______  ____ |  | __ \______   \ ____ _____  |  \_____   \
/   \  __\_  __ \/  _ \|  |/ /  |       _// __ \\__  \ |  |  /   __/
\    \_\  \  | \(  <_> )    <   |    |   \  ___/ / __ \|  |_|   |   
 \______  /__|   \____/|__|_ \  |____|_  /\___  >____  /____/___|   
        \/                  \/         \/     \/     \/     <___>   
""",
                color="yellow",
            )
        )
        print(color_message(message="Bot has started", color="green"))

        self.load_extensions()
        self.run(token)

    def load_extensions(self):
        self.unloaded_cogs = []

        for cog in os.listdir("./cogs"):
            if cog.endswith(".py"):
                try:
                    self.load_extension(name=f"cogs.{cog[:-3]}")
                    print(color_message(message=f"Loaded {cog[:-3]} cog", color="blue"))

                except Exception as e:
                    print(
                        color_message(
                            message=f"Failed to load {cog[:-3]} cog. Traceback: ",
                            color="red",
                        )
                        + str(e)
                    )
                    self.unloaded_cogs.append(cog[:-3])

    async def on_ready(self):
        print(color_message(message=f"Logged in as {self.user}!", color="green"))

        await self.change_presence(
            status=nextcord.Status.online,
            activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="You"),
        )
