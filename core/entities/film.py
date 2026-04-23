from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Film:
    id: Optional[int] = None
    title: str = ""
    episode_id: Optional[int] = None
    opening_crawl: Optional[str] = None
    director: Optional[str] = None
    producer: Optional[str] = None
    release_date: Optional[str] = None
    character_ids: List[int] = None
    planet_ids: List[int] = None

    def __post_init__(self):
        if self.character_ids is None:
            self.character_ids = []
        if self.planet_ids is None:
            self.planet_ids = []