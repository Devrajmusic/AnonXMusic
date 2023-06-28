from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "https://t.me/timepassgroup01")
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "https://t.me/dangerous_fighter_clan_0")
OWNER_USERNAME = getenv("OWNER_USERNAME", "https://t.me/taitangamerz")
OWNER_USERNAME = getenv("OWNERR_USERNAME", "https://t.me/taitangamer")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐌ᴏɪ 𝐋ᴜᴠ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 𝐅ᴇᴀᴛᴜʀᴇ 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ 𝐒ᴇᴛᴛɪɴɢ ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚ 𝐀ᴅᴅ 𝐌ᴇ 𝐌ᴏɪ 𝐋ᴜᴠ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝐌ᴀɴᴛᴀɪɴᴇʀ ✨", url=f"https://t.me/taitangamer",
            ),
            InlineKeyboardButton(
                text="🔎 𝐇ᴇʟᴘ 🔎", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 𝐒ᴜᴘᴘᴏʀᴛ 💫", url=f"https://t.me/DXDREAMBIG",
            ),
            InlineKeyboardButton(
                text="🍁 𝐔ᴘᴅᴀᴛᴇ 🍁", url=f"https://t.me/taitanoffice",
            )
        ],
        [
            InlineKeyboardButton(
                text="❄️ 𝐎ᴡɴᴇʀ ❄️",
                url=f"https://t.me/Wine_killerxd",
            )
        ],
     ]
    return buttons
