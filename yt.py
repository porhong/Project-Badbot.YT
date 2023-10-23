from pytube import YouTube
from aiogram import Bot, Dispatcher, types, executor
import os
import random
import string


bot = Bot(token="6620810299:AAGl04UJrW4qe5CNYuCiIC_gDMpkPeDzAuw")
dp = Dispatcher(bot)
def ytdl(link):
    t = random.choice(string.ascii_letters)
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename= t +".mp4")
    return t

@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
  await message.reply('''Hello 🙋‍♂️, Welcome to Badbot.YT''')


@dp.message_handler()
async def chat(message: types.Message):
    try:
        link = message.text
        v = ytdl(link)
        file = v.strip()+".mp4"
        print(file)
        source = open(file, "rb")
        await bot.send_document(message.chat.id,document=source)
        os.remove(file)
    except:
        pass

async def main() -> None:
    """"Entry Point"""
    await dp.start_polling(bot)

if __name__ == "__main__":
  executor.start_polling(dp)