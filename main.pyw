# Подключаю библиотеку aiogram для создания телеграм-бота
from aiogram import types, Bot, Dispatcher, executor
import config
import time

# Импортирую переменные российских акций финансового сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.finance_sector_RU.stocks_finance_sector import stocks_finance_name, stocks_finance_rub

# Импортирую переменные российских акций IT-сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.IT_sector_RU.stocks_IT_sector import IT_name, IT_rub

# Импортирую переменные российских акций потребительского сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.basic_sector_RU.stocks_basic_sector import stocksBasic_name, stocksBasic_data

# Импортирую переменные российскиз акций промышленного сектора из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.industrial_sector.stocks_industrial_sector import stocks_industrial_name, \
    stocks_industrial_rub

# Импортирую переменные российских акций из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocksRU.medicine_sector_RU.medicine_sectorRU import medicine_sector_name, medicine_sector_rub

# Импортирую переменные китайских акций из моего модуля, где происходит основной парсинг
from WarrenBuffetBot.stocks_China.stock_China import li_auto_name, li_auto_usd, baidu_name, baidu_usd, JD_name, JD_usd, \
    bilibili_name, bilibili_usd, tencent_name, tencent_usd, nio_name, nio_usd, xpeng_name, xpeng_usd

# Импортирую переменные с названиями криптовалют и их котировками из моего модуля, где происходит основной парсинг
from cryptocurrencies.crypto import bnb_name, bnb_usd, bitcoin_dollar, ethereum_dollar, litecoin_dollar, cardano_dollar, \
    xrp_dollar, doge_dollar, tether_name, tether_usd, solana_name, solana_usd, terra_name, terra_usd, uniswap_name, \
    uniswap_usd, polkadot_name, polkadot_usd, avalanche_name, avalanche_usd, chainlink_name, chainlink_usd, tron_name, \
    tron_usd, shiba_name, shiba_usd, ethereumClassic_name, ethereumClassic_usd

# Импортирую переменные курса валют из моего модуля, где происходит основной парсинг
from currency.currency import dollar_rub, euro_rub



# Импортирую переменные американских акций из моего модуля, где происходит основной парсинг
from stocksUSA.stocks_USA import stock_USA_1_name, stock_USA_2_name, stock_USA_1_dollar, stock_USA_2_dollar, \
    stock_USA_3_name, stock_USA_3_dollar, stock_USA_4_name, stock_USA_4_dollar, stock_USA_5_name, stock_USA_5_dollar, \
    stock_USA_6_name, stock_USA_6_dollar, stock_USA_7_name, stock_USA_7_dollar, stock_USA_8_name, stock_USA_8_dollar, \
    stock_USA_9_name, stock_USA_9_dollar, stock_USA_10_name, stock_USA_10_dollar, stock_USA_11_name, \
    stock_USA_11_dollar, stock_USA_12_name, stock_USA_12_dollar, stock_USA_13_name, stock_USA_13_dollar, \
    stock_USA_14_name, stock_USA_14_dollar, usa_names, usa_prices

# Импортирую переменные мировых индексов из моего модуля, где происходит основной парсинг
from world_indexes.world_indexes import MOEX_index_name, MOEX_index_rub, SnP500_index_name, SnP500_index, \
    NASDAQ_index_name, NASDAQ_index, SHANGAI_index_name, SHANGAI_index, array_index, prices_index

# Создаю бота, используя секретный токен(он находится в файле config), который дал нам @BotFather
bot = Bot(config.TOKEN)

# Создаю диспетчера, который отслеживает взаимодействие бота с пользователем
dp = Dispatcher(bot)

# Начинаю описывать функционал показа котировочных значений
async def show_USD_RUB():
    '''
    :return: Показ пользователю валютной пары USD/RUB
    '''
    text = '💵 Курс доллара ➡️'
    await bot.send_message(message.chat.id, text=text + str(dollar_rub))

async def show_EUR_RUB():
    '''
    :return: Показ пользователю валютной пары EUR/RUB
    '''
    text = '💶 Курс евро ➡️'
    await bot.send_message(message.chat.id, text=text + str(euro_rub))


async def show_Basic_RU():
    '''
    :return: Показ пользователю котровок акций реального сектора РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for basic in range(len(stocksBasic_name)):
        await bot.send_message(message.chat.id, text=stocksBasic_name[basic] + context + stocksBasic_data[stocksBasic_name[basic]] + RUB)

async def show_IT_RU():
    '''
    :return: Показ пользователю котровок акций IT-сектора РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for IT in range(len(IT_name)):
        await bot.send_message(message.chat.id, text=IT_name[IT] + context + IT_rub[IT_name[IT]] + RUB)

async def show_Finance_RU():
    '''
    :return: Показ пользователю котировок акций финансового сектора РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for finance in range(len(stocks_finance_name)):
        await bot.send_message(message.chat.id, text=stocks_finance_name[finance] + context + stocks_finance_rub[stocks_finance_name[finance]] + RUB)

async def show_Industrial_RU():
    '''
    :return: Показ пользователю котировок акций индустриального сектора РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for industrial in range(len(stocks_industrial_name)):
        await bot.send_message(message.chat.id,
                               text=stocks_industrial_name[industrial] + context + stocks_industrial_rub[
                                   stocks_industrial_name[industrial]] + RUB)

async def show_Medicine_RU():
    '''
    :return: Показ пользователю котировок акций здравоохранительного сектора РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for medicine in range(len(medicine_sector_name)):
        await bot.send_message(message.chat.id, text=medicine_sector_name[medicine] + context + medicine_sector_rub[
            medicine_sector_name[medicine]] + RUB)

async def show_realEstate_RU():
    '''
    :return: Показ пользователю котировок акций сектора - недвижимость РФ
    '''
    context = '➡️'
    RUB = ' RUB'
    for realEstate in range(len(stocks_industrial_name)):
        await bot.send_message(message.chat.id, text=stocks_industrial_name[realEstate] + context + stocks_industrial_rub[
            stocks_industrial_name[realEstate]] + RUB)


# Дескриптор(диспетчер отслеживает все стартовые нажатия на кнопки)
@dp.message_handler(commands=['start'])
async def bot_start(message: types.message):
    '''
    :param message:
    :return: Запуск меню бота
    '''
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currency_button = types.KeyboardButton('💰 Курс валют')
    stocks_button = types.KeyboardButton('💸 Курс акций')
    cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
    information_button = types.KeyboardButton('⚙️ Разработчик')

    markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)

    await bot.send_message(message.chat.id, 'Уоррен Баффетт приветствует тебя в мире инвестиций, {0.first_name}'.format(message.from_user), reply_markup=markup)


# Декскриптор - обработчик данных от пользователя
@dp.message_handler(content_types=['text'])
async def process_menu(message: types.message):
    '''
    :param message:
    :return: Обработчик функционала меню
    '''
    if message.chat.type == 'private':

        if message.text == '💰 Курс валют':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            dollar_button = types.KeyboardButton('💵 USD/RUB')
            euro_button = types.KeyboardButton('💶 EUR/RUB')
            back_button = types.KeyboardButton('◀️Назад')

            markup.add(dollar_button, euro_button, back_button)

            await bot.send_message(message.chat.id, '🕑 Загружаю курсы валют\n 🟩Загрузка...', reply_markup=markup)

        if message.text == '💵 USD/RUB':

            await show_USD_RUB()

        if message.text == '💶 EUR/RUB':

            await show_EUR_RUB()

        if message.text == '◀️Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            currency_button = types.KeyboardButton('💰 Курс валют')
            stocks_button = types.KeyboardButton('💸 Курс акций')
            cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
            information_button = types.KeyboardButton('⚙️ Разработчик')

            markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)

            await bot.send_message(message.chat.id, '◀️Назад', reply_markup=markup)

        if message.text == '💸 Курс акций':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            rus_stocks = types.KeyboardButton('🇷🇺 Акции')
            usa_stocks = types.KeyboardButton('🇺🇸 Акции')
            china_stocks = types.KeyboardButton('🇨🇳 Акции')
            world_indexes = types.KeyboardButton('🌆 Мировые индексы')
            back_button = types.KeyboardButton('◀️Назад')

            markup.add(rus_stocks, usa_stocks, china_stocks, world_indexes, back_button)

            await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        if message.text == '🇷🇺 Акции':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            basic_sector_rus = types.KeyboardButton('🧃 Потребительский сектор 🇷🇺')
            IT_sector_rus = types.KeyboardButton('📱 IT сектор 🇷🇺')
            finance_sector_rus = types.KeyboardButton('🏦 Финансовый сектор 🇷🇺')
            industrial_sector_rus = types.KeyboardButton('⛰ Промышленный сектор 🇷🇺')
            realEstate_sector_rus = types.KeyboardButton('🏙 Недвижимость 🇷🇺')
            medicine_sector_rus = types.KeyboardButton('💊 Медицина 🇷🇺')
            back_button = types.KeyboardButton('◀️Назад')

            markup.add(basic_sector_rus, IT_sector_rus, finance_sector_rus, industrial_sector_rus, realEstate_sector_rus, medicine_sector_rus, back_button)

            await bot.send_message(message.chat.id, text='🕑Загрузка', reply_markup=markup)

        if message.text == '🧃 Потребительский сектор 🇷🇺':

            await show_Basic_RU()

        if message.text == '📱 IT сектор 🇷🇺':

            await show_IT_RU()

        if message.text == '🏦 Финансовый сектор 🇷🇺':

            await show_Finance_RU()

        if message.text == '⛰ Промышленный сектор 🇷🇺':

            await show_Industrial_RU()

        if message.text == '🏙 Недвижимость 🇷🇺':

            await show_realEstate_RU()

        if message.text == '💊 Медицина 🇷🇺':

            await show_Medicine_RU()

        if message.text == '◀️Назад':

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            rus_stocks = types.KeyboardButton('🇷🇺 Акции')
            usa_stocks = types.KeyboardButton('🇺🇸 Акции')
            china_stocks = types.KeyboardButton('🇨🇳 Акции')
            world_indexes = types.KeyboardButton('🌆 Мировые индексы')
            back_button = types.KeyboardButton('◀️Назад')

            markup.add(rus_stocks, usa_stocks, china_stocks, world_indexes, back_button)

            await bot.send_message(message.chat.id, '🕑Загрузка', reply_markup=markup)

        if message.text == '🇺🇸 Акции':

            form = '🟢'
            context = '➡️'
            DOl = ' $'

            for usa_company in range(len(usa_names)):
                await bot.send_message(message.chat.id, text=form + usa_names[usa_company] + form + context + usa_prices[usa_names[usa_company]] + DOl)

        if message.text == '🇨🇳 Акции':

            context = '➡️'
            DOl = ' $'

            await bot.send_message(message.chat.id, text='Загружаю котировки лидеров торгов 🇨🇳')
            time.sleep(0.5)
            await bot.send_message(message.chat.id, text=str(li_auto_name) + context + str(li_auto_usd) + DOl)
            await bot.send_message(message.chat.id, text=str(baidu_name) + context + str(baidu_usd) + DOl)
            await bot.send_message(message.chat.id, text=str(JD_name) + context + str(JD_usd) + DOl)
            await bot.send_message(message.chat.id, text=str(bilibili_name) + context + str(bilibili_usd) + DOl)
            await bot.send_message(message.chat.id, text=str(tencent_name) + context + str(tencent_usd) + DOl)
            await bot.send_message(message.chat.id, text=str(nio_name) + context + str(nio_usd) +  DOl)
            await bot.send_message(message.chat.id, text=str(xpeng_name) + context + str(xpeng_usd) + DOl)


        if message.text == '🌆 Мировые индексы':

            index = '🟢'
            context = '➡️'

            for indexes in range(len(array_index)):
                await bot.send_message(message.chat.id, text=index + array_index[indexes] + index + context + prices_index[array_index[indexes]])

        if message.text == '◀️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            currency_button = types.KeyboardButton('💰 Курс валют')
            stocks_button = types.KeyboardButton('💸 Курс акций')
            cryptocurrency_button = types.KeyboardButton('💎 Курс криптовалют')
            information_button = types.KeyboardButton('⚙️ Разработчик')

            markup.add(currency_button, stocks_button, cryptocurrency_button, information_button)

            await bot.send_message(message.chat.id, '🕑Загружаю', reply_markup=markup)


        if message.text == '💎 Курс криптовалют':

            context = '➡'
            char = '🔷'
            USD = ' $'

            await bot.send_message(message.chat.id, '🕐🔜 Загружаю криптобазу...')
            time.sleep(0.5)
            await bot.send_message(message.chat.id, text='🔷BTC-USD🔷 ➡️' + str(bitcoin_dollar) + USD)
            await bot.send_message(message.chat.id, text='🔷ETH-USD🔷 ➡️' + str(ethereum_dollar) + USD)
            await bot.send_message(message.chat.id, text='🔷LTC-USD🔷 ➡️' + str(litecoin_dollar) + USD)
            await bot.send_message(message.chat.id, text='🔷ADA-USD🔷 ➡️' + str(cardano_dollar) + USD)
            await bot.send_message(message.chat.id, text='🔷XRP-USD🔷 ➡️' + str(xrp_dollar) + USD)
            await bot.send_message(message.chat.id, text='🔷DOGE-USD🔷 ➡️' + str(doge_dollar) + USD)
            await bot.send_message(message.chat.id, text=char + str(bnb_name) + char + context + str(bnb_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(tether_name) + char + context + str(tether_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(solana_name) + char + context +str(solana_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(terra_name) + char + context + str(terra_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(uniswap_name) + char + context + str(uniswap_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(polkadot_name) + char + context + str(polkadot_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(avalanche_name) + char + context + str(avalanche_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(chainlink_name) + char + context + str(chainlink_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(tron_name) + char + context + str(tron_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(shiba_name) + char + context + str(shiba_usd) + USD)
            await bot.send_message(message.chat.id, text=char + str(ethereumClassic_name) + context + str(ethereumClassic_usd) + USD)

        if message.text == '⚙️ Разработчик':

            await bot.send_message(message.chat.id, text='🌐 Разработчик: Миллер Ян Станиславович\n🏙 Студент НИУ ВШЭ, МИЭМ Информационная безопасность\n📚Уч.группа: БИБ211')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True)