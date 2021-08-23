from .repository import Repo
from domains import Box
import logging
import urllib.request


class TG(Repo):

    def post_box(self, box: Box, receiver: str, music=False) -> None:
        logging.info('post_music_box start')
        logging.debug(box.photo.__str__())
        logging.debug(box.photo.__str__())
        photo = urllib.request.urlopen(box.photo.url)
        self.connect.send_photo(chat_id=receiver, photo=photo, caption=box.text)
        if music:
            logging.debug(f'post_music_box: sounds count {len(box.sounds)}')
            for sound in box.sounds:
                logging.debug(sound.__str__())
            #     audio = urllib.request.urlopen(sound.url)
            #     self.connect.send_audio(chat_id=receiver, audio=audio, title=sound.title)

    def post_picture_box(self):
        pass

