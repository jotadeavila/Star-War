from typing import List, Optional
from core.entities.character import Character
from core.entities.planet import Planet
from core.entities.film import Film
from core.repositories.character_repository import CharacterRepository
from core.repositories.planet_repository import PlanetRepository
from core.repositories.film_repository import FilmRepository


class StarWarsService:
    def __init__(
        self,
        character_repo: CharacterRepository,
        planet_repo: PlanetRepository,
        film_repo: FilmRepository
    ):
        self._character_repo = character_repo
        self._planet_repo = planet_repo
        self._film_repo = film_repo

    def list_characters(self, name_filter: Optional[str] = None) -> List[Character]:
        return self._character_repo.get_all(name_filter)

    def get_character(self, character_id: int) -> Optional[Character]:
        return self._character_repo.get_by_id(character_id)

    def create_character(self, character: Character) -> Character:
        return self._character_repo.create(character)

    def list_planets(self) -> List[Planet]:
        return self._planet_repo.get_all()

    def create_planet(self, planet: Planet) -> Planet:
        return self._planet_repo.create(planet)

    def list_films(self) -> List[Film]:
        return self._film_repo.get_all()

    def create_film(self, film: Film) -> Film:
        return self._film_repo.create(film)

    def get_films_by_character(self, character_id: int) -> List[Film]:
        return self._film_repo.get_by_character_id(character_id)