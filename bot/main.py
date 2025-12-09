from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "🌱 Hello! I am Eco Assistant.\n"
        "I can help you reduce your ecological footprint!"
    )

@dp.message(Command("eco_tip"))
async def eco_tip(message: types.Message):
    await message.answer("♻ Eco Tip: Sort your waste to reduce pollution!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
