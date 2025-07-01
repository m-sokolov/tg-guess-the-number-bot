import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# Load token and web app URL
TOKEN = os.getenv("TOKEN")  # Set in Render or .env
WEBAPP_URL = "https://m-sokolov.github.io/tg-guess-game-web/"  # Replace with your actual GitHub Pages URL

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Play",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer("Welcome! Ready to play 'Guess the Number'? 👇", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
