import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.handlers import MessageHandler

# Get token and webapp URL
TOKEN = os.getenv("TOKEN")
WEBAPP_URL = "https://yourusername.github.io/your-repo-name/"  # Replace with your actual URL

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Define handler function
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Play",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await message.answer("Welcome! Ready to play 'Guess the Number'? 👇", reply_markup=keyboard)

async def main():
    # Register handler manually
    dp.message.register(start_handler, F.text == "/start")

    # Start polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
