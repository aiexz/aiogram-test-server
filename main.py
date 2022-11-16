import asyncio
import io
import logging
import os

import aiogram
import server

bot = aiogram.Bot(token=os.getenv("TOKEN"), server=server.TELEGRAM_TEST)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: aiogram.types.Message):
    await message.answer("Hello world on test side!")


@dp.message_handler(content_types=aiogram.types.ContentType.DOCUMENT)
async def document(message: aiogram.types.Message):
    file = io.BytesIO()
    await message.document.download(destination_file=file)
    file.name = message.document.file_name
    await message.answer_document(document=file)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()


asyncio.run(main())
