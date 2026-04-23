from dataclasses import dataclass
from typing import Optional


@dataclass
class Planet:
    id: Optional[int] = None
    name: str = ""
    climate: Optional[str] = None
    terrain: Optional[str] = None
    population: Optional[str] = None
    gravity: Optional[str] = None
    diameter: Optional[str] = None