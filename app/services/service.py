from repositories import DB, VK, TG
from drivers import VKConnect, TGConnect, SQLine
import logging


class Service(object):


    def __init__(self, context):
        logging.debug('Initialize service MoveMusic')
        self.db_rep = DB(SQLine().connect(context))
        self.vk_rep = VK(VKConnect().connect(context))
        self.tg_rep = TG(TGConnect().connect(context))