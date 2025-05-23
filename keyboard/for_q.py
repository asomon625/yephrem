from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

mounth = {
	"Январь": 31,
	"Февраль": 28,
	"Март": 31,
	"Апрель": 30,
	"Май": 31,
	"Июнь": 30,
	"Июль": 31,
	"Август": 31,
	"Сентябрь": 30,
	"Октябрь": 31,
	"Ноябрь": 30,
	"Январь": 31
}

def get_days_count(m):
	result = mounth.get(m, None)
	if result is not None:
		return result
	else:
		raise Exception("Такого месяца не существует!")

def get_mounth():
	builder = InlineKeyboardBuilder()

	for i in list(mounth.keys()):
		builder.add(
			InlineKeyboardButton(text=i, callback_data=f"mounth_{i}")
		)

	builder.adjust(3)

	return builder.as_markup()

def get_days(m="Январь"):
	builder = InlineKeyboardBuilder()

	builder.row(
		InlineKeyboardButton(text="◀️", callback_data=f"back_{m}"),
		InlineKeyboardButton(text=m, callback_data="answer_mounth"),
		InlineKeyboardButton(text="▶️", callback_data=f"next_{m}")
	)

	for i in range(1, get_days_count(m) + 1):
		builder.add(
			InlineKeyboardButton(text=str(i), callback_data=f"day_{m}_{i}")
		)

	builder.adjust(3)


	return builder.as_markup()

def get_notes(day, mounth, year=2025):
	builder = InlineKeyboardBuilder()
	builder.row(
		InlineKeyboardButton(text="Добавить заметку", callback_data=f"add_{day}_{mounth}_{year}")
	)

	return builder.as_markup()
