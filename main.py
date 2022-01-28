import telebot
from telebot import types

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Наличие товаров(Вейпинг)")
    item2 = types.KeyboardButton("Наличие товаров(Электроника)")
    item3 = types.KeyboardButton("Адреса")
    item4 = types.KeyboardButton("О боте")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Привет, {0.first_name}".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "Наличие товаров(Вейпинг)":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            creep = types.KeyboardButton("Одноразки")
            creep1 = types.KeyboardButton("Боксмоды")
            creep2 = types.KeyboardButton("Поды")
            creep3 = types.KeyboardButton("Картриджи")
            creep4 = types.KeyboardButton("Расходники")
            creep5 = types.KeyboardButton("Жидкости")
            creep6 = types.KeyboardButton("Назад")
            markup.add(creep, creep1, creep2, creep3, creep4, creep5, creep6)
            bot.send_message(message.chat.id, "Cписок товаров", reply_markup=markup)

        elif message.text == "Адреса":
            bot.send_message(message.chat.id, "Точка выдачи находится по адресу: г.Хабаровск, улица Зионов, 2689")
        elif message.text == "О боте":
            bot.send_message(message.chat.id, "Бот создан как онлайн-каталог ассортимента")
        elif message.text == "Наличие товаров(Электроника)":
            bot.send_message(message.chat.id, "Наушники Apple Airpods Clone, цена 2400р")
            p = open('C:/Users/feede/Documents/pythonProject/ufdu.png', 'rb')
            bot.send_photo(message.chat.id, p)
        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item1 = types.KeyboardButton("Наличие товаров(Вейпинг)")
            item2 = types.KeyboardButton("Наличие товаров(Электроника)")
            item3 = types.KeyboardButton("Адреса")
            item4 = types.KeyboardButton("О боте")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)
        elif message.text == "Одноразки":
            bot.send_message(message.chat.id, "Одноразовая электронная сигарета ElfBar puff 1200 \nЦена: 650р")
            p = open('C:/Users/feede/Documents/pythonProject/elf800.jpg', 'rb')
            bot.send_photo(message.chat.id, p)

            bot.send_message(message.chat.id, "Одноразовая электронная сигарета ElfBar puff 800 \nЦена: 550р")
            p1 = open('C:/Users/feede/Documents/pythonProject/elf1500.jpg', 'rb')
            bot.send_photo(message.chat.id, p1)

            bot.send_message(message.chat.id, "Одноразовая электронная сигарета Ijoy Xeon \nЦена: 550р")
            p2 = open('C:/Users/feede/Documents/pythonProject/IjoyXeon.jpg', 'rb')
            bot.send_photo(message.chat.id, p2)


bot.polling(none_stop=True)
