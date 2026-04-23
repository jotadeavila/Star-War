from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.character import Character


class CharacterRepository(ABC):
    @abstractmethod
    def get_all(self, name_filter: Optional[str] = None) -> List[Character]:
        pass

    @abstractmethod
    def get_by_id(self, character_id: int) -> Optional[Character]:
        pass

    @abstractmethod
    def create(self, character: Character) -> Character:
        pass