from dataclasses import dataclass
from typing import Optional


@dataclass
class Music(object):
    url: str
    title: Optional[str] = None
