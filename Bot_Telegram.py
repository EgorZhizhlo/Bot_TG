import telebot

from bs4 import BeautifulSoup
import requests

from telebot import types

bot = telebot.TeleBot("2041476775:AAFXO2UlfuYN5xDJctDRIDGAVzev1MBoApA")


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

tovar = types.KeyboardButton("🛒Товар")
videoobzor = types.KeyboardButton("📹Видео-обзор")
otziv = types.KeyboardButton("✍Отзывы")
exit = types.KeyboardButton("❌Выход")

markup.add(tovar, videoobzor, otziv, exit)


mag_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

dns_m = types.KeyboardButton("🏪ДНС")
mvideo_m = types.KeyboardButton("🏪Мвидео")
eldorado_m = types.KeyboardButton("🏪Эльдорадо")
citilink_m = types.KeyboardButton("🏪Ситилинк")
e_catalog_m = types.KeyboardButton("🏪Е-Каталог")

mag_markup.add(dns_m, mvideo_m, eldorado_m, citilink_m, e_catalog_m, exit)


mark_s = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

st = types.KeyboardButton("Start")

mark_s.add(st)


mark_c = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

min_c = types.KeyboardButton("Минимальная цена")

mark_c.add(min_c)


yes_n_mark = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

yes = types.KeyboardButton("Yes")
no = types.KeyboardButton("No")

yes_n_mark.add(yes, no)

S_or_E = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

S_or_E.add(st, exit)


@bot.message_handler(content_types=['text'])
def Start_F(message):
    while message.text == 'Привет' or message.text == 'Hello' or message.text == 'Hi' \
            or message.text == 'Приветик' or message.text == 'привет' or message.text == 'hello' or message.text == 'hi' \
            or message.text == 'приветик' or message.text == 'Start' or message.text == 'start':
        bot.send_message(message.chat.id,
                         "Привет, {0.first_name}!\nЯ- Бот <b>{1.first_name}</b>. Я  помогу выбрать тебе товар."
                         "\nДавай определимся, что ты хотел бы найти."
                         "\nЕсли вы хотите найти товар, введите или нажмите на '🛒Товар'"
                         "\nЕсли вы хотите посмотреть видеообзор, введите или нажмите на '📹Видео-обзор'"
                         "\nЕсли вы хотите просмотреть все отзывы по товару введите или нажмите на '✍Отзывы'"
                         .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, Function_selection)
        break
    else:
        bot.send_message(message.chat.id,
                         "{0.first_name}, к сожаления я тебя не понял, "
                         "общатся со мной следует только используя команды.".format(message.from_user,
                                                                                    bot.get_me()), parse_mode='html',
                         reply_markup=mark_s)


def Function_selection(message):
    if message.text == '🛒Товар' or message.text == 'Товар'.lower() or message.text == 'Выбор товара'.lower():
        bot.send_message(message.chat.id, '🏪Выберите магазин введя или нажав желаемый магазин или нажав "❌Выход" покинуть поиск.'
                                          'Если хотите остановить общение, то введите или нажмите "❌Выход"',
                         reply_markup=mag_markup)
        bot.register_next_step_handler(message, Shop_selection)
    elif message.text == '📹Видео-обзор' or message.text == 'Видео-обзор'.lower() or message.text == 'Видеообзор'.lower() \
            or message.text == 'Обзор'.lower():
        bot.send_message(message.chat.id, 'Напишите товар, на который вы бы хотели найти видеообзор.')
        bot.register_next_step_handler(message, Video_print)

    elif message.text == '✍Отзывы' or message.text == 'Отзывы':
        bot.send_message(message.chat.id, 'Напишите товар, на который вы бы хотели найти отзыв.')
        bot.register_next_step_handler(message, Otziv_print)
    elif message.text == '❌Выход' or message.text == 'Выход' or message.text == 'выход':
        bot.send_message(message.chat.id, 'До новых встреч, {0.first_name}! '
                                          'Для начала общения '
                                          'воспльзуйся клавиатурой-подсказкой, нажав на "Start".'.format(message.from_user,
                                          bot.get_me()), parse_mode='html', reply_markup=mark_s)


def Shop_selection(message):
    text_soobsh = 'Напишите модель товара, который желаете купить.'
    if message.text == '🏪ДНС' or message.text == 'ДНС' or message.text == 'Днс':
        bot.send_message(message.chat.id, text_soobsh)
        bot.register_next_step_handler(message, Dns_product)
    elif message.text == '🏪Мвидео' or message.text == 'Мвидео':
        bot.send_message(message.chat.id, text_soobsh)
        bot.register_next_step_handler(message, Mvideo_product)
    elif message.text == '🏪Эльдорадо' or message.text == 'Эльдорадо':
        bot.send_message(message.chat.id, text_soobsh)
        bot.register_next_step_handler(message, Eldorado_product)
    elif message.text == '🏪Ситилинк' or message.text == 'Ситилинк':
        bot.send_message(message.chat.id, text_soobsh)
        bot.register_next_step_handler(message, Citilink_product)
    elif message.text == '🏪Е-Каталог' or message.text == 'Е-Каталог' or message.text == 'ЕКаталог':
        bot.send_message(message.chat.id, text_soobsh + ' Марку товара писать на английском языке и без ключевых слов.'
                                                        ' Пример ключевых слов:'
                                                        ' Монитор, Клавиатура и т.д.')
        bot.register_next_step_handler(message, E_Katalog)
    elif message.text == '❌Выход' or message.text == 'Выход' or message.text == 'выход':
        bot.send_message(message.chat.id, 'До новых встреч, {0.first_name}! '
                                          'Для начала общения '
                                          'воспльзуйся клавиатурой-подсказкой, нажав на "Start".'.format(message.from_user,
                                          bot.get_me()), parse_mode='html', reply_markup=mark_s)


@bot.message_handler(content_types=['text'])
def Dns_product(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.replace(" ", '+')
    corect_url = f"https://www.dns-shop.ru/search/?q={corect_slov_polz}"
    bot.send_message(message.chat.id, 'Вот подборка товаров в магазине ДНС'
                                          f' :{corect_url}. Если вы желаете узнать цену данного товара в других магазина, '
                                          ' воспользуйтесь клавиатурой-подсказкой, нажав на "Лучшая цена"', reply_markup=mark_c)
    bot.register_next_step_handler(message, min_a_max)


def Mvideo_product(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.replace(" ", '%20')
    corect_url = f"https://www.mvideo.ru/product-list-page?q={corect_slov_polz}"
    bot.send_message(message.chat.id, 'Вот подборка товаров в магазине МВИДЕО'
                                      f' :{corect_url}. Если вы желаете узнать цену данного товара в других магазина, '
                                          ' воспользуйтесь клавиатурой-подсказкой, нажав на "Лучшая цена"', reply_markup=mark_c)
    bot.register_next_step_handler(message, min_a_max)

def Eldorado_product(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.replace(" ", '%20')
    corect_url = f"https://www.eldorado.ru/search/catalog.php?q={corect_slov_polz}"
    bot.send_message(message.chat.id, 'Вот подборка товаров в магазине ЭЛЬДОРАДО'
                                      f' :{corect_url}. Если вы желаете узнать цену данного товара в других магазина, '
                                          ' воспользуйтесь клавиатурой-подсказкой, нажав на "Лучшая цена"', reply_markup=mark_c)
    bot.register_next_step_handler(message, min_a_max)


def Citilink_product(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.replace(" ", '+')
    corect_url = f"https://www.citilink.ru/search/?text={corect_slov_polz}&menu_id=162"
    bot.send_message(message.chat.id, 'Вот подборка товаров в магазине СИТИЛИНК'
                                      f' :{corect_url}. Если вы желаете узнать цену данного товара в других магазина, '
                                          ' воспользуйтесь клавиатурой-подсказкой, нажав на "Лучшая цена"', reply_markup=mark_c)
    bot.register_next_step_handler(message, min_a_max)


def min_a_max(message):
    if message.text == "Лучшая цена" or message.text == "Лцена" or message.text == "Best price" \
            or message.text == "best prise" or message.text == "лучшая цена" or message.text == "лцена":
        bot.send_message(message.chat.id, ' Марку товара писать на английском языке и без ключевых слов.'
                                                        ' Пример ключевых слов:'
                                                        ' Монитор, Клавиатура и т.д.')
        bot.register_next_step_handler(message, E_Katalog)


def E_Katalog(message):
    global corect_url
    slova_polz = message.text
    corect_slov_polz = slova_polz.upper().replace(" ", '-')
    corect_url = f"https://www.e-katalog.ru/{corect_slov_polz}.htm"

    def get_h(url, params=None):
        req = requests.get(url, params=params)
        return req

    def get_c(html1):
        soup = BeautifulSoup(html1, 'html.parser')
        items = soup.find_all('div', class_="common-table-div")

        tov = []

        for item in items:
            tov.append({
                'name_t': item.find('h1', itemprop="name").get_text(),
                'l_price': item.find('span', itemprop="lowPrice").get_text().replace('\xa0', ' '),
                'h_price': item.find('span', itemprop="highPrice").get_text().replace('\xa0', ' ')
            })
        return tov

    def parse():
        html1 = get_h(corect_url)
        if html1.status_code == 200:
            tov = get_c(html1.text)
            for i in range(len(tov)):
                propars_tov = tov[i]
                ima_tov = propars_tov['name_t']
                min_cena_tov = propars_tov['l_price']
                max_cena_tov = propars_tov['h_price']
            bot.send_message(message.chat.id, "Минимальная цена найденого товара"
                                              f" {ima_tov}: {min_cena_tov} руб. Максимальная: {max_cena_tov} руб."
                                              " Желаете увидеть ссылку? Воспользуйтесь клавиатурой-подсказкой"
                                              ", выбрав 'Лучшая цена'", reply_markup=yes_n_mark)
            bot.register_next_step_handler(message, yes_or_no)
        else:
            bot.send_message(message.chat.id, 'ERROR')

    parse()


def yes_or_no(message):
    if message.text == 'Yes' or message.text == 'Да':
        bot.send_message(message.chat.id, f'Вот ваша ссылка: {corect_url}.', reply_markup=mark_s)
        bot.register_next_step_handler(message, Start_F)
    elif message.text == 'No' or message.text == 'Нет':
        bot.send_message(message.chat.id, 'Хорошо, желаешь продолжить?', reply_markup=S_or_E)
        bot.register_next_step_handler(message, Start_F)


def Video_print(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.lower().replace(" ", '+')
    corect_url = f"https://www.youtube.com/results?search_query={corect_slov_polz}"
    bot.send_message(message.chat.id, f"Ссылка на видеообзор по запросу {slova_polz}: {corect_url}."
                                      " Для продолжения воспользуйтесь клавиатурой-подсказкой, выбрав"
                                      " '🛒Товар', '📹Видео-обзор', '✍Отзывы' и '❌Выход'")


def Otziv_print(message):
    slova_polz = message.text
    corect_slov_polz = slova_polz.lower().replace(" ", '-')
    corect_url = f"https://www.e-katalog.ru/review/{corect_slov_polz}/"
    bot.send_message(message.chat.id, f"Ссылка на отзывы по запросу {slova_polz}: {corect_url}."
                                      " Для продолжения воспользуйтесь клавиатурой-подсказкой, выбрав"
                                      " '🛒Товар', '📹Видео-обзор', '✍Отзывы' и '❌Выход'")


bot.polling(none_stop=True)