
import asyncio

import os
import config
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint
@app.on_message(
    filters.regex(r"(سورس مين|سورس|السورس|سورسي|TNT)")
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/db3b085fbe1ca9ed1e530.jpg",
        caption=f"""𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "قـناه الدعـم ", url=f"https://t.me/I1_35"), 
                
                    InlineKeyboardButton(
                        "جــروب الـدعم ", url=f"https://t.me/UC_IU"),
                ],[
                    InlineKeyboardButton(
                        "⌞𝙎َِ𝙊َِ𝙐َِ𝙍َِ𝘾َِ𝙀 َِ𝙈َِ𝙊َِ𝙍3َِ𝘽⌝", url=f"https://t.me/UC_IU"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



