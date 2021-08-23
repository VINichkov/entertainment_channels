from drivers.singleton import MetaSingleton
import telebot
import logging


class TGConnect(metaclass=MetaSingleton):
    tg = None

    def connect(self, context=None):
        if context is None and self.tg is None:
            return None
        if self.tg is None:
            logging.debug('Initialize TGConnect driver')
            self.tg = telebot.TeleBot(token=context['config'].get('settings', 'telegram_bot_token'), parse_mode=None)
        return self.tg
