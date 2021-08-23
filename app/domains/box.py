from dataclasses import dataclass, field
from typing import Optional
from .photo import Photo
from .music import Music


@dataclass
class Box(object):
    text: Optional[str] = None
    photo: Optional[Photo] = None
    id: Optional[int] = None
    sounds: list[Music] = field(default_factory=list)
    date: Optional[int] = None


