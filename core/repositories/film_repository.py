from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.film import Film


class FilmRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Film]:
        pass

    @abstractmethod
    def get_by_id(self, film_id: int) -> Optional[Film]:
        pass

    @abstractmethod
    def create(self, film: Film) -> Film:
        pass

    @abstractmethod
    def get_by_character_id(self, character_id: int) -> List[Film]:
        pass

    @abstractmethod
    def get_by_planet_id(self, planet_id: int) -> List[Film]:
        pass