from .service import Service
import logging


class MoveMusic(Service):
    __source = None

    def call(self, source: str, channel_sources: str, receiver: str) -> None:
        self.__source = source
        logging.info('Run service MoveMusic')
        self.__list_music_boxes = self.vk_rep.get_music_box(source)
        self.__last_post = self.db_rep.last_post(source)
        logging.info('Finished service MoveMusic')
        self.__selected_box = self.__choose_box()
        logging.debug(f'MoveMusic: selected box {self.__selected_box.__str__()}')
        self.db_rep.create(
            post=music_box_to_post(
                music_box=self.__selected_box,
                source=source,
                channel_sources=channel_sources
            )
        )
