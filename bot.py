import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")
WEBAPP_URL = "https://m-sokolov.github.io/tg-guess-game-web/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Play",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer("Welcome! Ready to play 'Guess the Number'? 👇", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
