from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_student
#@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.text.lower() == "привет":
        await bot.send_message(message.chat.id, "Привет!",reply_markup=kb_student)
    if message.text.lower() == "пока":
        await bot.send_message(message.chat.id, "Пока")
def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(text)