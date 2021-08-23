from domains import box_to_post
from repositories import MUSIC_BOX
from .service import Service
import logging


class Move(Service):
    __list_boxes = None
    __last_post = None
    __source = None
    __selected_box = None

    def call(self, source: str, channel_sources: str, receiver: str, music=False) -> None:
        self.__source = source
        logging.info('Run service Move')
        self.__list_boxes = self.vk_rep.get_boxes(source_group=source, cl=MUSIC_BOX if music else 'None')
        self.__last_post = self.db_rep.last_post(source)
        logging.info('Finished service Move')
        self.__selected_box = self.__choose_box()
        logging.debug(f'Move: selected box {self.__selected_box.__str__()}')
        if self.__selected_box is not None:
            self.db_rep.create(
                post=box_to_post(
                    box=self.__selected_box,
                    source=source,
                    channel_sources=channel_sources
                )
            )

            self.tg_rep.post_box(box=self.__selected_box, receiver=receiver, music=music)

    def __choose_box(self):

        def get_id(box):
            return box.id

        logging.debug('Start choose a box')
        if self.__last_post is None:
            logging.debug("Didn't get record from DB for group {group}".format(group=self.__source))
            return min(self.__list_boxes, key=get_id)
        else:
            logging.debug(f"Got a {self.__source}")
            sorted_music_boxes = sorted(self.__list_boxes, key=get_id)
            logging.debug(sorted_music_boxes)
            for item in sorted_music_boxes:
                if item.id > self.__last_post.id_post:
                    return item
