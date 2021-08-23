from dataclasses import dataclass
from typing import Optional


@dataclass
class Post(object):
    id_post: int
    data: Optional[int]
    source: str
    channel_source: Optional[str]