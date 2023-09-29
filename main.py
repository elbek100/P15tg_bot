import os
import types
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from time import sleep
import asyncio

from code import get_picture

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    first_name = message.from_user.first_name
    await message.answer(f'hello {first_name}')


@dp.message(lambda msg: msg.text == '/news')
async def news(message: Message):
    while True:
        await get_picture()
        picture = FSInputFile('new.png', filename='screenshot')
        await message.answer_photo(picture)
        sleep(10800)

async def main():
    bot = Bot(os.getenv("BOT_API"))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
