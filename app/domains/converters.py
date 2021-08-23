import logging
from .post import Post
from .box import Box


def box_to_post(box: Box, source: str, channel_sources: str) -> Post:
    logging.debug('music_box_to_post start')
    logging.debug(f'convert music_box = [{box}]')
    return Post(id_post=box.id,
                data=box.date,
                source=source,
                channel_source=channel_sources)
