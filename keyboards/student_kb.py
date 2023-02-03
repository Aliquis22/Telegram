from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.types import callback_query

b1 = KeyboardButton('/rasp')
b2 = KeyboardButton('/start')

kb_student = ReplyKeyboardMarkup(resize_keyboard=True)

kb_student.add(b1).add(b2)

