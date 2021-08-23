from drivers import SQLine
import logging
import configparser
import sqlite3
import sys
import os


def init_env(context):
    logging.debug('Start load ENV')
    config_path = os.path.join(os.path.abspath(os.curdir), 'share/secrets.ini')
    logging.debug(config_path)
    config = configparser.ConfigParser()
    config.read(config_path)
    logging.debug(config.sections())
    logging.info('ENV loaded')
    context['config'] = config


def init_db(context):
    logging.debug('Checking if a table exists')
    driver = SQLine().connect(context)
    cur = driver.cursor()
    try:
        cur.execute('''CREATE TABLE posts
                               (id integer, data integer, source text, channel_source text)''')
        driver.commit()
        logging.info('The table created')
    except sqlite3.OperationalError:
        logging.info('The table is exist')


def disconnect():
    SQLine().close_connect()
    logging.info('Finished')
