from core.entities.character import Character
from core.entities.planet import Planet
from core.entities.film import Film


class TestCharacterEntity:
    def test_character_creation(self):
        character = Character(
            id=1,
            name="Luke Skywalker",
            height="172",
            mass="77",
            gender="Masculino"
        )
        assert character.id == 1
        assert character.name == "Luke Skywalker"
        assert character.film_ids == []

    def test_character_with_films(self):
        character = Character(
            name="Leia Organa",
            film_ids=[1, 2, 3]
        )
        assert character.film_ids == [1, 2, 3]


class TestPlanetEntity:
    def test_planet_creation(self):
        planet = Planet(
            id=1,
            name="Tatooine",
            climate="Árido",
            terrain="Desierto"
        )
        assert planet.name == "Tatooine"
        assert planet.population is None


class TestFilmEntity:
    def test_film_creation(self):
        film = Film(
            id=1,
            title="Una Nueva Esperanza",
            episode_id=4,
            director="George Lucas"
        )
        assert film.title == "Una Nueva Esperanza"
        assert film.character_ids == []
        assert film.planet_ids == []