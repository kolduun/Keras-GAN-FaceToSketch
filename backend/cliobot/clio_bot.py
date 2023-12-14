import telebot
import os
from telebot import types
from random import randint
from typing import Optional
from typing import List
from dotenv import load_dotenv


class ClioTelegramBotHandler:
    """
    ClioTelegramBotHandler contain the basic logic of the telegram bot:
    Handling events, Sending requests.
    Singleton, as only one instance of the bot can be launched.
    """

    _instance = None

    def __init__(self) -> None:
        load_dotenv()
        self.sd_token: Optional[str] = os.environ.get('SD_KEY')
        self.photo_url: Optional[str] = os.environ.get('LOGO_URL')

        self.bot = telebot.TeleBot(os.environ.get('TG_KEY'))
        self.start()

    def __new__(cls) -> object:
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def start(self):
        answer_message_base: List[str] = ['С Вами приятно общаться, но я не на столько умный, чтобы дать Вам ответ:(',
                                          'Мне стоит на это что-то отвечать...?',
                                          'Мне очень жаль, но общение с пользователями - не моя компетенция:(',
                                          'Я не умею осознано общаться с пользователем, но, надеюсь, мои создатели работают над этим....',
                                          'Я могу отправить Вам картинку кота....']

        @self.bot.message_handler(commands=['start'])
        def answer_on_start(message):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            keyboard.add(types.KeyboardButton('Можно кота?'), types.KeyboardButton('Информация о боте'))
            keyboard.add(types.KeyboardButton('Сгенерируй лицо'))
            self.bot.send_message(message.chat.id, f"Здравствуй, {message.from_user.first_name}!", reply_markup=keyboard)

        @self.bot.message_handler()
        def chat_with_bot(message):
            if 'сгенерируй' in message.text.lower():
                self.bot.send_message(message.chat.id, "Подождите, я думаю.....")
                self.bot.send_photo(message.chat.id, photo=lambda x: x,
                               caption='Готово! Я своё отработал...')
            elif 'пирожки' in message.text.lower():
                self.bot.send_message(message.chat.id, "Пирожки с котятами...")
            elif message.text == 'Можно кота?':
                self.bot.send_photo(message.chat.id, photo=os.environ.get('LOGO_URL'), caption='ДА! Теперь Вы кот!')
            elif message.text == 'Информация о боте':
                self.bot.send_message(message.chat.id, "Мы команда Клио и это наш чат-бот со встроенной нейросетью."
                                                  " Мы считаем, что нейронные сети не должны заменять художников, а "
                                                  "наоборот - помогать им. Наш бот генерирует мини-урок по рисованию человеческой"
                                                  " головы. Чтобы начать работу просто напиши боту \"сгенерируй\" и он нарисует для тебя"
                                                  " пошаговый урок по рисованию человеческой головы!")
            elif 'привет' in message.text.lower():
                self.bot.send_message(message.chat.id,
                                 f"Здравствуй, {message.from_user.first_name}! Начнем работу? Напиши мне, и я сгенерирую мини-урок")
            else:
                self.bot.send_message(message.chat.id, answer_message_base[randint(0, len(answer_message_base) - 1)])


        self.bot.polling(none_stop=True)


def run_clio_telegram_bot():
    return ClioTelegramBotHandler()
