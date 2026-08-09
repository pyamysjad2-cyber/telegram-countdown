import os
import asyncio
from datetime import datetime, date
from zoneinfo import ZoneInfo
from telegram import Bot

TOKEN = os.environ["8842311265:AAF-T509aLZBNpLad2uGMZ6gZD8oOD4TuHA"]
CHAT_ID = os.environ["1004448100571"]

TARGET_DATE = date(2026, 8, 21)

MESSAGE = """🔥 موفقیت اتفاقی نیست؛ نتیجه‌ی تلاش‌های کوچکی است که هر روز تکرار می‌کنی.

🎯 روزشمار کنکور

⏳ {days} روز تا ۳۰ مرداد"""

async def send_message():
    bot = Bot(TOKEN)

    today = datetime.now(ZoneInfo("Asia/Tehran")).date()
    days = max((TARGET_DATE - today).days, 0)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=MESSAGE.format(days=days)
    )

asyncio.run(send_message())
