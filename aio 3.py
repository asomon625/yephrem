import os
import logging
import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram import Bot, Dispatcher, types, F
from keyboard.for_q import *
from aiogram.filters.command import Command, CommandObject
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

logging.basicConfig(level=logging.INFO)

TOKEN = "7674408763:AAFP_wiQ6HeFlhDbmRNRzO561_JROxIucNg"
dp = Dispatcher()
bot = Bot(token=TOKEN)

notes = {}

class AddNote(StatesGroup):
  text = State()
  walet = State()

def wallet():
  builder = InlineKeyboardBuilder()
  builder.button(text=f"Перевести в доллары", callback_data=f"usdt")
  builder.button(text=f"Перевести в тенге", callback_data=f"tenge")
  builder.button(text=f"Перевести в белорусские рубли", callback_data=f"bel")
  builder.button(text=f"Перевести в фунт стерлингов", callback_data=f"pount")
  builder.button(text=f"Перевести в юани", callback_data=f"juan")
  builder.button(text=f"Перевести в евро", callback_data=f"euro")
  builder.adjust(2)
  return builder.as_markup()

@dp.message(Command("start"))
async def start(message):
  await message.answer(f"Привет, это бот конвертёр валют, выберите валюту, в которую хотите перевести суммму.", reply_markup = wallet())

@dp.callback_query(F.data.startswith(f"usdt"))
async def usdt(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в доллар.")
  await state.update_data(walet = "usdt")
  await state.set_state(AddNote.text)

@dp.callback_query(F.data.startswith(f"tenge"))
async def tenge(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в тенге.")
  await state.update_data(walet = "tenge")
  await state.set_state(AddNote.text)

@dp.callback_query(F.data.startswith(f"bel"))
async def bel(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в белорусские рубли.")
  await state.update_data(walet = "bel")
  await state.set_state(AddNote.text)

@dp.callback_query(F.data.startswith(f"pount"))
async def pount(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в фунты стерлингов.")
  await state.update_data(walet = "pount")
  await state.set_state(AddNote.text)

@dp.callback_query(F.data.startswith(f"juan"))
async def juan(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в юани.")
  await state.update_data(walet = "juan")
  await state.set_state(AddNote.text)

@dp.callback_query(F.data.startswith(f"euro"))
async def euro(call, state):
  await call.message.answer("Введите сумму (в рублях) которую хотите перевести в евро.")
  await state.update_data(walet = "euro")
  await state.set_state(AddNote.text)

@dp.message(AddNote.text)
async def note(message, state):
    walet = await state.get_data()
    walet = walet["walet"]
    text = float(message.text)
    await state.clear()
    await message.answer(f"Вы ввели сумму: {text} руб.")
    usdt = text/80
    juan = text/ 11
    bel = text/24
    euro = text/90
    tenge = text*6.3
    pount = text/107
    if walet == "usdt":
      await message.answer(f"{text} руб. в доллары это {usdt} долларов(а)")
    elif walet == "tenge":
      await message.answer(f"{text} руб. в тенге это {tenge} тенге")
    elif walet == "bel":
      await message.answer(f"{text} руб. в белорусские рубли это {bel} белорусских рублей(я)")
    elif walet == "euro":
      await message.answer(f"{text} руб. в евро это {euro} евро")
    elif walet == "pount":
      await message.answer(f"{text} руб. в фунты стерлингов это {pount} футнтов стерлингов(а")
    elif walet == "juan":
      await message.answer(f"{text} руб. в юани это {juan} юаней(я)")




async def main():
  await dp.start_polling(bot)

if __name__ == "__main__":
  asyncio.run(main())