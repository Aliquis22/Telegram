from aiogram import types, Dispatcher
from keyboards import kb_student
from datetime import datetime, date, time
from create_bot import dp, bot
import os, json, datetime
date =  str(date.today())
day = datetime.datetime.today().weekday()
if day == 0:
    day="Понедельник"
elif day == 1:
    day="Вторник"
elif day == 2:
    day="Среда"
elif day == 3:
    day="Четверг"
elif day == 4:
    day="Пятница"
elif day == 5:
    day="Суббота"
else:
    day="Воскресение"
with open("rasp.json", encoding = "utf8") as file:
    data = json.load(file)
keys = list(data.keys())

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Выберете что хотите сделать ", reply_markup=kb_student)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему")

async def button_reaction1(message: types.Message):
    k=0
    s= day + " (" + date +")" + 2*"\n"
    if str(keys[0]) == "code":
        s += "Сегодня занятий нет"
    for i in range(0,len(data)-1):
        if date == data[str(i)]['start'][:10] :
            start = data[str(i)]['start'][11:16]
            end  = data[str(i)]['end'][11:16]
            disciplina = data[str(i)]['disciplina'][0]['full_name']
            if len(data[str(i)]['lichnost']) != 0 :
                teacher = data[str(i)]['lichnost'][0]['title']
            else:
                teacher = ""
            if data[str(i)]['place'] != None:
                corp  = "к." + data[str(i)]['place']['korpus']
                aud = "ауд." + data[str(i)]['place']['nomer']
            else:
                corp  = ""
                aud = ""
            if i!=0 and disciplina != str(data[str(i-1)]['disciplina']):
                s+=str("*" + disciplina + "*" +"\n")
                s+=str(start + " - " + end +"\n")
                s+=str(teacher + "\n")
                s += str(corp + " " + aud + "\n")
                s += "\n"
            elif i==0:
                s += str( "*" + disciplina + "*" + "\n")
                s+=str(teacher + "\n")
                s += str(corp + " " + aud + "\n")

            else:
                s += str(teacher + "\n")
                s += str(corp + " " + aud + "\n")
                s +=('\n')

    await bot.send_message(message.from_user.id, "*Расписание на сегодня*" + "\n" + s, parse_mode="Markdown", reply_markup=kb_student)
    if day == "Воскресение":
        await bot.send_message(message.from_user.id, "Сегодня занятий нет", parse_mode="Markdown",
                               reply_markup=kb_student)


# async def button_reaction2(call: types.callback_query):
#     s = "Расписание на эту неделю:" +"\n"
#     s+=day + " " + date + "\n"
#     await bot.answer_callback_query(call.id)
#     for i in range(0,len(data)-1):
#         if date == data[str(i)]['start'][:10]:
#             start = data[str(i)]['start'][11:16]
#             end  = data[str(i)]['end'][11:16]
#             disciplina = data[str(i)]['disciplina'][0]['full_name']
#             if len(data[str(i)]['lichnost']) != 0 :
#                 teacher = data[str(i)]['lichnost'][0]['title']
#             else:
#                 teacher = ""
#             if data[str(i)]['place'] != None:
#                 corp  = "к." + data["0"]['place']['korpus']
#                 aud = "ауд." + data["0"]['place']['nomer']
#             else:
#                 corp  = ""
#                 aud = ""
#             if ((i!=0) and disciplina != data[str(i-1)]['disciplina'][0]['full_name'])  :
#                 s+=str(disciplina + "\n")
#                 s+=str(start + " - " + end +"\n")
#                 s+=str(teacher + "\n")
#                 s += str(corp + " " + aud + "\n")
#             else:
#                  s+=str(teacher + "\n")
#                  s += str(corp + " " + aud + "\n")
#     await bot.send_message(call.message.chat.id, "Функция в разработке")
def register_handlers_student(dp : Dispatcher):
    dp.register_message_handler(command_start,commands=['start', 'help'])
    dp.register_message_handler(button_reaction1, commands=['rasp'])






