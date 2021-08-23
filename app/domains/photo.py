from dataclasses import dataclass
from typing import Optional


@dataclass
class Photo(object):
    url: str
    text: Optional[str]
