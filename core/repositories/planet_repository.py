from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.planet import Planet


class PlanetRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Planet]:
        pass

    @abstractmethod
    def get_by_id(self, planet_id: int) -> Optional[Planet]:
        pass

    @abstractmethod
    def create(self, planet: Planet) -> Planet:
        pass