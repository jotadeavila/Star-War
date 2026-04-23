from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Character:
    id: Optional[int] = None
    name: str = ""
    height: Optional[str] = None
    mass: Optional[str] = None
    hair_color: Optional[str] = None
    skin_color: Optional[str] = None
    eye_color: Optional[str] = None
    birth_year: Optional[str] = None
    gender: Optional[str] = None
    film_ids: List[int] = None

    def __post_init__(self):
        if self.film_ids is None:
            self.film_ids = []