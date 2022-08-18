import telebot
from telebot import types
import choice_brand

bot = telebot.TeleBot('...')


@bot.message_handler(commands=['buslik'])
def buslik_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go to site', url='https://buslik.by/'))
    bot.send_message(message.chat.id,
                     'Here you can place an online order in the buslik.by online store', reply_markup=markup)


@bot.message_handler(commands=['detmir'])
def detmir_site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go to site', url='https://detmir.by/'))
    bot.send_message(message.chat.id,
                     'Here you can place an online order in the detmir.by online store', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button_1 = types.KeyboardButton('Buslik store')
    button_2 = types.KeyboardButton('Detmir store')
    button_3 = types.KeyboardButton('General base of two stores')
    markup.add(button_1, button_2, button_3)
    send_mess = f"<b>Hello, {message.from_user.first_name}!</b>"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    markup = None
    final_message = 'These are all items as your request'

    if get_message_bot == 'main menu':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_1 = types.KeyboardButton('Buslik store')
        button_2 = types.KeyboardButton('Detmir store')
        button_3 = types.KeyboardButton('General base of two stores')
        markup.add(button_1, button_2, button_3)
        final_message = 'You have returned to the main menu, please make your selection'

    elif get_message_bot == 'buslik store':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_1 = types.KeyboardButton('Huggies buslik store')
        button_2 = types.KeyboardButton('Pampers buslik store')
        button_3 = types.KeyboardButton('Yokosun buslik store')
        button_4 = types.KeyboardButton('Watashi buslik store')
        button_5 = types.KeyboardButton('All diapers buslik store')
        button_6 = types.KeyboardButton('Main menu')
        markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
        final_message = "Buslik popular children's goods store"

    elif get_message_bot == 'detmir store':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_1 = types.KeyboardButton('Regular diapers')
        button_2 = types.KeyboardButton('Diapers - panties')
        button_3 = types.KeyboardButton('Main menu')
        markup.add(button_1, button_2, button_3)
        final_message = 'Detmir popular store with reasonable prices'

    elif get_message_bot == 'general base of two stores':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_1 = types.KeyboardButton('Huggies general base')
        button_2 = types.KeyboardButton('Pampers general base')
        button_3 = types.KeyboardButton('Yokosun general base')
        button_4 = types.KeyboardButton('Watashi general base')
        button_5 = types.KeyboardButton('All diapers general base')
        button_6 = types.KeyboardButton('Main menu')
        markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
        final_message = 'You will receive information about products from two stores'

    elif get_message_bot == 'regular diapers':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_1 = types.KeyboardButton('Huggies detmir diapers')
        button_2 = types.KeyboardButton('Pampers detmir diapers')
        button_3 = types.KeyboardButton('Yokosun detmir diapers')
        button_4 = types.KeyboardButton('Manu detmir diapers')
        button_5 = types.KeyboardButton('All detmir diapers')
        button_6 = types.KeyboardButton('Main menu')
        markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
        final_message = 'You will receive information about the products of the selected brand'

    elif get_message_bot == 'huggies detmir diapers':
        @bot.message_handler(content_types=['text'])
        def huggies_detmir_diapers(message):
            for i in choice_brand.brand_huggies():
                if len(choice_brand.brand_huggies()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        huggies_detmir_diapers(message)

    elif get_message_bot == 'pampers detmir diapers':
        @bot.message_handler(content_types=['text'])
        def pampers_detmir_diapers(message):
            for i in choice_brand.brand_pampers():
                if len(choice_brand.brand_pampers()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        pampers_detmir_diapers(message)

    elif get_message_bot == 'yokosun detmir diapers':
        @bot.message_handler(content_types=['text'])
        def yokosun_detmir_diapers(message):
            for i in choice_brand.brand_yokosun():
                if len(choice_brand.brand_yokosun()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        yokosun_detmir_diapers(message)

    elif get_message_bot == 'manu detmir diapers':
        @bot.message_handler(content_types=['text'])
        def manu_detmir_diapers(message):
            for i in choice_brand.brand_manu():
                if len(choice_brand.brand_manu()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        manu_detmir_diapers(message)

    elif get_message_bot == 'all detmir diapers':
        @bot.message_handler(content_types=['text'])
        def all_detmir_diapers(message):
            for i in choice_brand.all_brand_regular():
                if len(choice_brand.all_brand_regular()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        all_detmir_diapers(message)

    elif get_message_bot == 'diapers - panties':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button_1 = types.KeyboardButton('Huggies detmir panties')
        button_2 = types.KeyboardButton('Pampers detmir panties')
        button_3 = types.KeyboardButton('Yokosun detmir panties')
        button_4 = types.KeyboardButton('Manu detmir panties')
        button_5 = types.KeyboardButton('All detmir panties')
        button_6 = types.KeyboardButton('Main menu')
        markup.add(button_1, button_2, button_3, button_4, button_5, button_6)
        final_message = 'You will receive information about the products of the selected brand'

    elif get_message_bot == 'huggies detmir panties':
        @bot.message_handler(content_types=['text'])
        def huggies_detmir_panties(message):
            for i in choice_brand.brand_huggies_pants():
                if len(choice_brand.brand_huggies_pants()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        huggies_detmir_panties(message)

    elif get_message_bot == 'pampers detmir panties':
        @bot.message_handler(content_types=['text'])
        def pampers_detmir_panties(message):
            for i in choice_brand.brand_pampers_pants():
                if len(choice_brand.brand_pampers_pants()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        pampers_detmir_panties(message)

    elif get_message_bot == 'yokosun detmir panties':
        @bot.message_handler(content_types=['text'])
        def yokosun_detmir_panties(message):
            for i in choice_brand.brand_yokosun_pants():
                if len(choice_brand.brand_yokosun_pants()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        yokosun_detmir_panties(message)

    elif get_message_bot == 'manu detmir panties':
        @bot.message_handler(content_types=['text'])
        def manu_detmir_panties(message):
            for i in choice_brand.brand_manu_pants():
                if len(choice_brand.brand_manu_pants()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        manu_detmir_panties(message)

    elif get_message_bot == 'all detmir panties':
        @bot.message_handler(content_types=['text'])
        def all_detmir_panties(message):
            for i in choice_brand.all_brand_pants():
                if len(choice_brand.all_brand_pants()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        all_detmir_panties(message)

    elif get_message_bot == 'huggies buslik store':
        @bot.message_handler(content_types=['text'])
        def huggies_buslik_store(message):
            for i in choice_brand.brand_huggies_stork():
                if len(choice_brand.brand_huggies_stork()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        huggies_buslik_store(message)

    elif get_message_bot == 'pampers buslik store':
        @bot.message_handler(content_types=['text'])
        def pampers_buslik_store(message):
            for i in choice_brand.brand_pampers_stork():
                if len(choice_brand.brand_pampers_stork()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        pampers_buslik_store(message)

    elif get_message_bot == 'yokosun buslik store':
        @bot.message_handler(content_types=['text'])
        def yokosun_buslik_store(message):
            for i in choice_brand.brand_yokosun_stork():
                if len(choice_brand.brand_yokosun_stork()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        yokosun_buslik_store(message)

    elif get_message_bot == 'watashi buslik store':
        @bot.message_handler(content_types=['text'])
        def watashi_buslik_store(message):
            for i in choice_brand.brand_watashi_stork():
                if len(choice_brand.brand_watashi_stork()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        watashi_buslik_store(message)

    elif get_message_bot == 'all diapers buslik store':
        @bot.message_handler(content_types=['text'])
        def all_diapers_buslik_store(message):
            for i in choice_brand.all_brand_regular():
                if len(choice_brand.all_brand_regular()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        all_diapers_buslik_store(message)

    elif get_message_bot == 'huggies general base':
        @bot.message_handler(content_types=['text'])
        def huggies_general_base(message):
            for i in choice_brand.brand_huggies_all():
                if len(choice_brand.brand_huggies_all()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        huggies_general_base(message)

    elif get_message_bot == 'pampers general base':
        @bot.message_handler(content_types=['text'])
        def pampers_general_base(message):
            for i in choice_brand.brand_pampers_all():
                if len(choice_brand.brand_pampers_all()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        pampers_general_base(message)

    elif get_message_bot == 'yokosun general base':
        @bot.message_handler(content_types=['text'])
        def yokosun_general_base(message):
            for i in choice_brand.brand_yokosun_all():
                if len(choice_brand.brand_yokosun_all()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        yokosun_general_base(message)

    elif get_message_bot == 'watashi general base':
        @bot.message_handler(content_types=['text'])
        def watashi_general_base(message):
            for i in choice_brand.brand_watashi_all():
                if len(choice_brand.brand_watashi_all()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        watashi_general_base(message)

    elif get_message_bot == 'all diapers general base':
        @bot.message_handler(content_types=['text'])
        def all_diapers_general_base(message):
            for i in choice_brand.general_brand_all():
                if len(choice_brand.general_brand_all()) > 0:
                    send_mess = f"Brand: {i[1]}\n{i[2]}\nSize: {i[3]}\n" \
                                f"Actual price: {i[4]} BYN | Old price: {i[5]} BYN\nStore: {i[6]}"
                    bot.send_message(message.chat.id, send_mess)
                else:
                    send_mess = 'No products found for this search'
                    bot.send_message(message.chat.id, send_mess)

        all_diapers_general_base(message)

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_1 = types.KeyboardButton('Buslik store')
        button_2 = types.KeyboardButton('Detmir store')
        button_3 = types.KeyboardButton('General base of two stores')
        markup.add(button_1, button_2, button_3)
        final_message = 'You have entered text that I do not know.\n' \
                        'Better use interactive buttons for correct text input.\n' \
                        'You have returned to the main menu, please make your selection'

    bot.send_message(message.chat.id, final_message, reply_markup=markup)


bot.polling(none_stop=True)
