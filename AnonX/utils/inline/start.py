from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀ᴅᴅ 𝐌ᴇ 𝐌ᴏɪ 𝐋ᴜᴠ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝐇ᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="𝐒ᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ 𝐀ᴅᴅ 𝐌ᴇ 𝐌ᴏɪ 𝐋ᴜᴠ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💫 𝐇ᴇʟᴩ 💫", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 𝐒ᴜᴩᴩᴏʀᴛ 💥", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="🥀 𝐔ᴘᴅᴀᴛᴇ 💥", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="♛ 𝐎ᴡɴᴇʀ ♛", user_id=OWNER
            )
        ],
     ]
    return buttons
