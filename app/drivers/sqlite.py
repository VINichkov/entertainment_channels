from drivers.singleton import MetaSingleton
import sqlite3
import logging


class SQLine(metaclass=MetaSingleton):
    sql = None

    def connect(self, context=None):
        if context is None and self.sql is None:
            return None
        if self.sql is None:
            logging.debug('Initialize SQLine driver')
            self.sql = sqlite3.connect(context['config'].get('settings', 'db_name'))
        return self.sql

    def close_connect(self):
        self.sql.close()
