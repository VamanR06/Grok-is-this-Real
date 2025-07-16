from constants import (
    COLORS,
    COLOR_GOOD,
    COLOR_NEUTRAL,
    COLOR_BAD,
)
import nextcord
from typing import List
import json, asyncio, aiohttp


def color_message(message: str, color: str = COLORS["default"]):
    color = COLORS.get(color, COLORS["default"])
    return color + message + "\033[0m"


def create_success_embed(title: str = "\u200b", description: str = "\u200b"):
    embed = nextcord.Embed(title=title, description=description, color=COLOR_GOOD)
    embed.set_thumbnail(
        url="https://media3.giphy.com/media/CaS9NNso512WJ4po0t/giphy.gif?cid=ecf05e47mgm8u6fljfxl5d5g0s01tp94qgn9exfwqvlpi3id&rid=giphy.gif&ct=s"
    )
    return embed


def create_warning_embed(title: str = "\u200b", description: str = "\u200b"):
    embed = nextcord.Embed(title=title, description=description, color=COLOR_NEUTRAL)
    embed.set_thumbnail(
        url="https://c.tenor.com/26pNa498OS0AAAAi/warning-joypixels.gif"
    )
    return embed


def create_error_embed(title: str = "\u200b", description: str = "\u200b"):
    embed = nextcord.Embed(title=title, description=description, color=COLOR_BAD)
    embed.set_thumbnail(
        url="https://i.gifer.com/origin/bf/bf2d25254a2808835e20c9d698d75f28_w200.gif"
    )
    return embed


async def send_webhook_message(
    url: str,
    username: str,
    content: str = None,
    embeds: List[dict] = None,
    avatarURL: str = None,
    req_type: str = "post",
):
    try:
        async with aiohttp.ClientSession(loop=asyncio.get_event_loop()) as session:
            async with session.__getattribute__(req_type)(
                url,
                json={
                    "content": content,
                    "username": username,
                    "embeds": embeds if embeds else None,
                    "avatar_url": avatarURL if avatarURL else None,
                },
            ) as response:
                return await response.json(content_type=None)

    except Exception as e:
        print(e)
        return None


def get_json_file(path: str):
    with open(path) as f:
        data = json.load(f)

    return data


def update_json_file(data: dict, path: str):
    with open(path, "w") as f:
        json.dump(data, f)
