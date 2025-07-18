import asyncio
import nextcord
from nextcord.ext import commands
from bot import Bot

from openai import OpenAI

from constants import XAI_API_KEY, XAI_BASE_URL, XAI_MODEL

client = OpenAI(
    api_key=XAI_API_KEY,
)


class Real(commands.Cog):
    def __init__(self, client: Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if (
            next((i for i in message.mentions if i.id == self.client.user.id), None)
            is None
        ):
            return
        
        if message.reference is None:
            message_to_check = message
            message_content = message.content.strip()

        else:
            try:
                message_to_check = await message.channel.fetch_message(
                    message.reference.message_id
                )

            except Exception:
                return
            
            message_content = message_to_check.content.strip()

        test_msg = message_content

        for i in message.mentions:
            test_msg = test_msg.replace(i.mention, i.name)

        if test_msg == "":
            return

        completion = client.chat.completions.create(
            model=XAI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a resourceful assistant who will prove or disprove the user",
                },
                {"role": "user", "content": message_content},
            ],
        )

        await message_to_check.reply(content=completion.choices[0].message.content)

        await message.add_reaction(emoji="👍")

        await asyncio.sleep(3)

        await message.remove_reaction(
            emoji="👍", member=message.guild.get_member(self.client.user.id)
        )


def setup(client: Bot):
    client.add_cog(Real(client))
