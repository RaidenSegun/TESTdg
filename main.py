from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random

from aiogram import Bot, Dispatcher
from config import token
import asyncio, logging


bot = Bot(token=token)
dp = Dispatcher()



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите один вариант", reply_markup=start_keyboard)


@dp.message(F.text == "Игра")
async def game(message: Message):
    await message.answer("Выберите", reply_markup=game_keyboards)


@dp.message(F.text.in_({"Камень", "Ножницы", "Бумага"}))
async def game_start(message: Message):
    if message.text == "Камень":
        await message.answer("Вы проиграли!")
    elif message.text == "Ножницы":
        await message.answer("Вы выиграли!")
    elif message.text == "Бумага":
        await message.answer("Ничья!")
    else:
        await message.answer("Выберите кнопку.")


@dp.message(F.text == "Рандомайзер")
async def random_(message: Message):
    lucky_number = random.choice(["Вы победили", "Вы проиграли", "Ничья"])
    await message.answer(f"{lucky_number}")


@dp.message(F.text == "Наши новости")
async def news(message: Message):
    await message.answer("Выберите кнопку", reply_markup=news_keyboards)


@dp.message(lambda message: message.text in {"О нас", "Адресс", "Наши курсы"})
async def news_(message: Message):
    if message.text == "О нас":
        await message.answer("Наша компания учит программистов")
    elif message.text == "Адресс":
        await message.answer("Наш адресс Томирис")
    elif message.text == "Наши курсы":
        await message.answer("Наши курсы предлагают\nBackend\nFrontend\nDesigner.")

start_keyboard = ReplyKeyboardMarkup(
    keyboard = [
       [KeyboardButton(text = "Игра"), KeyboardButton(text = "Наши новости")]
    ], resize_keyboard=True, one_time_keyboard=True
)


game_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Камень"), KeyboardButton(text = "Ножницы"), KeyboardButton(text = "Бумага")],
        [KeyboardButton(text = "Рандомайзер")]
    ], resize_keyboard=True
)


news_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "О нас"), KeyboardButton(text = "Адресс"), KeyboardButton(text = "Наши курсы")]
    ], resize_keyboard=True
)

async def main():
    logging.basicConfig(level="INFO")
    await dp.start_polling(bot)




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот приостановлен!")