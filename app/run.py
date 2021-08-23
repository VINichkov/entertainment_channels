from config import init_env, init_db, disconnect
import aioschedule as schedule
import time

from services import Move
# import vk_advanced_api
import asyncio
import logging
#from vk_android.android import VkAndroidApi


async def start():
    logging.basicConfig(format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        handlers=[
                            logging.FileHandler('share/app.log'),
                            logging.StreamHandler()
                        ],
                        level=logging.DEBUG)
    context = {}
    logging.info('Start')
    init_env(context)
    init_db(context)

    # vk = VkAndroidApi(login=context['config'].get('settings', 'login'),
    #                   password=context['config'].get('settings', 'pass'))  # или token="token",secret="secret"
    # secret, token = vk.secret, vk.token
    # print(vk.method("audio.get", owner_id=-128918799))

    def condition(x: str) -> bool:
        return x.find('mapping') == 0

    bots_conf = filter(condition, context['config'].sections())

    for bot in tuple(bots_conf):
        service = Move(context)
        service.call(source=context['config'].get(bot, 'vk_group'),
                     channel_sources=bot,
                     receiver=context['config'].get(bot, 'tg_channel'))

    #disconnect()
    logging.info('Finished')
    # rep_vk = VK(driver=VKConnect().connect(context),
    #             source_group=context['config'].get('first_bot', 'vk_group'))
    #
    # for msg in rep_vk.get_last_music_box():
    #     print(msg)
    # bot = telebot.TeleBot(token=context['config'].get('settings', 'telegram_bot_token'), parse_mode=None)
    # bot.send_message(chat_id=context['config'].get('first_bot', 'tg_channel'),
    #                 text=vk.wall.get(domain='musicpovenamm')['items'][0]['text'])

asyncio.run(start())
# schedule.every().hour.do(start)
# loop = asyncio.get_event_loop()
# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     loop.run_until_complete(schedule.run_pending())
#     time.sleep(60)
