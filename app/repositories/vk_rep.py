from .repository import Repo
from vk_api import audio
from domains import Box, Photo, Music
import logging
MUSIC_BOX = 'Music'


def choose_size(sizes_hash):
    logging.debug('choose_size start')
    result = None
    result = sizes_hash['x']
    if result is None:
        result = sizes_hash['y']
    if result is None:
        result = sizes_hash['r']
    if result is None:
        result = sizes_hash['z']
    if result is None:
        result = sizes_hash['q']
    if result is None:
        result = max(sizes_hash, key=lambda x: x['height'])
    return result


class VK(Repo):
    __audio = None

    def __init__(self, driver):
        self.connect = driver.get_api()
        self.driver = driver

    def get_boxes(self, source_group, cl):
        if cl == MUSIC_BOX:
            self.__audio = audio.VkAudio(vk=self.driver)
        logging.debug('VK rep: start get_music_box ')
        items = self.connect.wall.get(domain=source_group)['items']
        logging.debug('VK rep: posts were gotten')
        if len(items) > 0:
            logging.debug(f'VK rep: posts count = {len(items)}')
            list_boxes = self.__convert_to_box_list(items, cl)
            if len(list_boxes) > 0:
                logging.debug(f'VK rep: valid posts count = {len(list_boxes)}')
                return list_boxes
        return None

    def __convert_to_box_list(self, items, cl) -> list:
        logging.debug('convert_to_box_list start')
        result = []
        logging.debug(f'convert_to_box_list: gotten {len(items)} items')
        if len(items) == 0:
            return result

        for item in items:
            if (item.get('attachments') is None or len(item.get('attachments')) == 0 or item.get('marked_as_ads') != 0
                    or item.get('copy_history') is not None or item.get('post_type') != 'post'):
                logging.debug(f"convert_to_box_list: item {item.get('id')} is not correct")
                continue
            box = Box()
            logging.debug(f'convert_to_box_list: {box.__str__()}')
            box.text = item.get('text')
            box.id = int(item.get('id'))
            box.date = int(item.get('date'))
            attachments = item.get('attachments')
            for attachment in attachments:
                if box.photo is None and attachment.get('type') == 'photo':
                    sizes_hash = self.__create_photo_sizes_hash(attachment.get('photo').get('sizes'))
                    photo = choose_size(sizes_hash)
                    box.photo = Photo(url=photo.get('url'), text=attachment.get('photo').get('text'))
                if attachment.get('type') == 'audio':
                    logging.debug(attachment)
                    box.sounds.append(Music(url=attachment.get('audio').get('url'), title=attachment.get('audio')
                                                  .get('title')))
            if (len(box.sounds) > 0 and cl == MUSIC_BOX
                    or box.photo is not None and cl != MUSIC_BOX and len(box.sounds) == 0):
                logging.debug(f"convert_to_music_box_list: item {item.get('id')} is correct")
                result.append(box)
        return result

    def __create_photo_sizes_hash(self, photo_sizes=None):
        logging.debug('create_photo_sizes_hash start')
        if photo_sizes is not None and len(photo_sizes) > 0:
            sizes_hash = {}
            for size in photo_sizes:
                sizes_hash[size['type']] = size
            return sizes_hash
        return None
