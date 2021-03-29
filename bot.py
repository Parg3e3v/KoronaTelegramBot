from covid import Covid # 2.1.6
import telebot
from telebot import types
import country_converter as coco
import flag


covid19 = Covid(source="worldometers")
bot = telebot.TeleBot('1244740181:AAGGMJ2_Mwa_MmVAFi3stofmF5cVJw1_qtY')

@bot.message_handler(commands=['start'])
def start(message):
    # Globals
    global IsChanging
    global notific
    global country
    global nowConfirmend
    global nowDeaths
    global id
    IsChanging = False
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Armenia')
    btn3 = types.KeyboardButton('Russia')
    btn4 = types.KeyboardButton('Japan')
    btn5 = types.KeyboardButton('Georgia')
    btn6 = types.KeyboardButton('USA')
    global buttons
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6]
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_msg = f'<b>Привет🙂 <em>{message.from_user.first_name} </em>!</b>\n<b>Я - <em>Корона Бот</em>, могу показать информацию про каронавирус🦠</b>\n' \
               f' <b>Нажми на любую из <em>кнопок</em>, чтобы получить <em>информацию </em>про каронавирус👇</b>\n<b> </b>\n<b>Если ты не нашёл имя той страны, которой хотел, просто пришли мне её!' \
               f'<em>(Только по Английски!)</em></b>\n<b></b>\n'\
               f'<b>Если возникли вопросы, напиши команду\n/help 🙂</b>'
    sti = open('stickers/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, send_msg, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    msg = f"<b>Help</b>❤️\n<b></b>\n"\
          f"/changebutton - <b>Поменять любую кнопку на новую😐</b>\n" \
          f"/list - <b>Имена всех <u>стран</u> и <u>месностей</u>, которые поддерживает бот🦠</b>\n" \
          f"/help - <b>Помощь</b>✅\n<b></b>\n"\
          f"<b>Если хочешь узнать информацию пор <em>стану</em>, имя которой не видишь ниже👇, то просто <em>отправь мне её!</em>📝</b>"
    stick = open('stickers/wanted.tgs', 'rb')
    bot.send_message(message.chat.id, msg, parse_mode='html')
    bot.send_sticker(message.chat.id, stick)

@bot.message_handler(commands=['changebutton'])
def changebutton(message):
    msg = f"<b>Хорошо😊.</b>\n<b>Теперь выбери, кокую кнопку хочешь поменять на новую👇</b>"
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("1", callback_data=1)
    item2 = types.InlineKeyboardButton("2", callback_data=2)
    item3 = types.InlineKeyboardButton("3", callback_data=3)
    item4 = types.InlineKeyboardButton("4", callback_data=4)
    item5 = types.InlineKeyboardButton("5", callback_data=5)
    item6 = types.InlineKeyboardButton("6", callback_data=6)
    item7 = types.InlineKeyboardButton("По умолчанию", callback_data="reset")

    markup.add(item1, item2, item3, item4, item5, item6, item7)

    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global IsChanging


    # Если потребуется ^_^
    # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
    #                           text="В разработке!!!")


    global buttons
    try:
        if call.message:
            if call.data == "reset":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=f"<b>Хорошо😊.</b>\n<b>Теперь выбери, кокую кнопку хочешь поменять на новую👇</b>",
                                      reply_markup=None, parse_mode='html')
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
                btn1 = types.KeyboardButton('Во всём мире')
                btn2 = types.KeyboardButton('Armenia')
                btn3 = types.KeyboardButton('Russia')
                btn4 = types.KeyboardButton('Japan')
                btn5 = types.KeyboardButton('Georgia')
                btn6 = types.KeyboardButton('US')
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
                msg = f"<b>Данные Обнавлены👍</b>"
                sticker = open("stickers/good.tgs", "rb")
                bot.send_message(call.message.chat.id, msg, reply_markup=markup, parse_mode='html')
                bot.send_sticker(call.message.chat.id, sticker)

            else:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= f"<b>Хорошо😊.</b>\n<b>Теперь выбери, кокую кнопку хочешь поменять на новую👇</b>",
                                      reply_markup=None, parse_mode='html')
                global data
                data = call.data
                txt = f"<b>Теперь отправь мне имя страны, которой хочешь заменить предыдущий текст ☺️</b>"

                IsChanging = True
                bot.send_message(call.message.chat.id, txt, parse_mode='html')



    except Exception as e:
        print(repr(e))

@bot.message_handler(commands=['news'])
def notif(message):
    # global notific
    # notific = True
    # mes = f"<b>Хорошо. Теперь пришли мне имя страны<em>(на Английском)</em>, уведомления о которой хочешь получить</b>"
    # bot.send_message(message.chat.id, mes, parse_mode='html')
    bot.send_message(message.chat.id, f"<u>В разработке!!</u>", parse_mode='html')


@bot.message_handler(commands=['list'])
def list(message):
    msg = f""
    all = covid19.list_countries()
    for i in all:
        if i == 'north america':
            bot.send_message(message.chat.id, f"<b>Загрузка🙂...</b>", parse_mode='html')
            st = open("stickers/working.tgs", "rb")
            bot.send_sticker(message.chat.id,st)
        if i == 'world':
            # bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=f"<b>Загрузка🙂!!!!...</b>", parse_mode='html')
            continue
        try:
            name = coco.convert(names=i, to='ISO2')
            fl = flag.flag(name)
        except ValueError:
            try:
                fl = flag.flag(i)
                # if fl == "🏴":
                #     fl = "🏁"
            except Warning:
                fl = "🏴"
            except ValueError:
                fl = "🏴"


        msg += f"<b>{i}</b> {fl},\n"
    bot.send_message(message.chat.id, msg, parse_mode='html')

@bot.message_handler(content_types=['text'])
def mess(message):
    global buttons
    global data
    global IsChanging
    global notific
    final_message = ""
    get_mess = message.text
    if IsChanging == False:
        if get_mess == "Во всём мире":
            deaths = covid19.get_total_deaths()
            confirmed = covid19.get_total_confirmed_cases()
            recovered = covid19.get_total_recovered()
            final_message = f"<b><em>Данные по всему миру 🏳️:</em></b>\n" \
                            f"<b>Последние данные:\n</b>" \
                            f"<b>Заболевших: </b>{confirmed}\n<b>Сметрей: </b> {deaths}\n<b>Исцелённых: </b>{recovered}"
        else:
            try:
                location = covid19.get_status_by_country_name(get_mess)
            except ValueError:
                    final_message = "Я нечего не нашёл"
                    st = open("stickers/what.tgs", "rb")
                    bot.send_sticker(message.chat.id, st)

        if final_message == "":
            name = coco.convert(names=location['country'], to='ISO2')
            fl = flag.flag(name)
            final_message = f"<b><em>{location['country']} </em> {fl} :</b>\n"\
                            f"<u>Данные по стране:</u>\n" \
                            f"Последние данные:\n<b>" \
                            f"Заболевших: </b>{location['confirmed']:,}\n<b>Новых заболевших: </b>{location['new_cases']}\n<b>Сметрей: </b> {location['deaths']:,}\n<b>Исцелённых: </b>{location['recovered']}"

        bot.send_message(message.chat.id, final_message, parse_mode='html')

    # elif notific == True:
    #     if get_mess == "Во всём мире":
    #         pass
    #     else:
    #         try:
    #             location = covid19.get_status_by_country_name(get_mess)
    #         except ValueError:
    #             final_message = "Ошибка❌"
    #             st = open("stickers/end.tgs", "rb")
    #             bot.send_sticker(message.chat.id, st)
    #             bot.send_message(message.chat.id, final_message, parse_mode='html')
    #
    #     if final_message == "":
    #         ms = f"Отлично. Уведомления включены!"
    #         bot.send_message(message.chat.id, ms, parse_mode='html')
    #         global country
    #         global nowConfirmend
    #         global nowDeaths
    #         global id
    #         id = message.chat.id
    #         nowDeaths = location['deaths']
    #         nowConfirmend = location['confirmed']
    #         country = get_mess
    #     notific = False

    else:
        if get_mess == "Во всём мире":
            buttons[int(data) - 1].text = get_mess
            final_message = "Во всём мире"
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(buttons[0], buttons[1], buttons[2], buttons[3], buttons[4], buttons[5])
            msg = f"<b>Данные Обнавлены👍</b>"
            sticker = open("stickers/good.tgs", "rb")
            bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')
            bot.send_sticker(message.chat.id, sticker)
            IsChanging = False
        else:
            try:
                location = covid19.get_status_by_country_name(get_mess)
            except ValueError:
                final_message = "Ошибка❌"
                st = open("stickers/end.tgs", "rb")
                bot.send_sticker(message.chat.id, st)
                bot.send_message(message.chat.id, final_message, parse_mode='html')
        if final_message == "":
            buttons[int(data) - 1].text = get_mess
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            markup.add(buttons[0],buttons[1],buttons[2],buttons[3],buttons[4],buttons[5])
            msg = f"<b>Данные Обнавлены👍</b>"
            sticker = open("stickers/good.tgs", "rb")
            bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')
            bot.send_sticker(message.chat.id,sticker)
            IsChanging = False


@bot.message_handler(content_types=['audio', 'video', 'document', 'location', 'contact', 'sticker', 'photo'])
def mess(message):
    final_message = "Ошибка❌"
    st = open("stickers/end.tgs", "rb")
    bot.send_sticker(message.chat.id, st)
    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop = True)



# while True:
#     global country
#     global nowConfirmend
#     global nowDeaths
#     global id
#
#     try:
#         location = covid19.get_status_by_country_name(country)
#         if location['confirmed'] > nowConfirmend:
#             ms = f"<b>В {country} число заболевших изменилось на <u>{location['confirmed'] - nowConfirmend}</u> !</b>"
#             bot.send_message(id, ms, parse_mode='html')
#             st2 = open("stickers/news.tgs", "rb")
#             bot.send_sticker(id, st2)
#             nowConfirmend = location['confirmed']
#
#         if location['deaths'] > nowDeaths:
#             ms = f"<b>В {country} число умерших изменилось на <u>{location['deaths'] - nowDeaths}</u> !</b>"
#             bot.send_message(id, ms, parse_mode='html')
#             st2 = open("stickers/news.tgs", "rb")
#             bot.send_sticker(id, st2)
#             nowDeaths = location['deaths']
#         else:
#             pass
#     except NameError:
#         continue
