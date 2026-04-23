from unittest.mock import Mock, MagicMock
from core.entities.character import Character
from core.entities.planet import Planet
from core.entities.film import Film
from core.services.starwars_service import StarWarsService


class TestStarWarsService:
    def setup_method(self):
        self.mock_character_repo = Mock()
        self.mock_planet_repo = Mock()
        self.mock_film_repo = Mock()
        self.service = StarWarsService(
            self.mock_character_repo,
            self.mock_planet_repo,
            self.mock_film_repo
        )

    def test_list_characters(self):
        expected = [
            Character(id=1, name="Luke Skywalker"),
            Character(id=2, name="Leia Organa")
        ]
        self.mock_character_repo.get_all.return_value = expected
        
        result = self.service.list_characters()
        
        assert result == expected
        self.mock_character_repo.get_all.assert_called_once_with(None)

    def test_list_characters_with_filter(self):
        expected = [Character(id=1, name="Luke Skywalker")]
        self.mock_character_repo.get_all.return_value = expected
        
        result = self.service.list_characters("Luke")
        
        assert result == expected
        self.mock_character_repo.get_all.assert_called_once_with("Luke")

    def test_create_character(self):
        character = Character(name="Han Solo")
        expected = Character(id=3, name="Han Solo")
        self.mock_character_repo.create.return_value = expected
        
        result = self.service.create_character(character)
        
        assert result == expected
        self.mock_character_repo.create.assert_called_once_with(character)

    def test_get_films_by_character(self):
        expected = [
            Film(id=1, title="Una Nueva Esperanza"),
            Film(id=2, title="El Imperio Contraataca")
        ]
        self.mock_film_repo.get_by_character_id.return_value = expected
        
        result = self.service.get_films_by_character(1)
        
        assert result == expected
        self.mock_film_repo.get_by_character_id.assert_called_once_with(1)