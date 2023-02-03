from aiogram import executor
from create_bot import dp
from handlers import student, other, admin

student.register_handlers_student(dp)
other.register_handlers_other(dp)
async def on_startup(_):
    print("Бот вышел в онлайн")

executor.start_polling(dp, skip_updates = True, on_startup=on_startup)