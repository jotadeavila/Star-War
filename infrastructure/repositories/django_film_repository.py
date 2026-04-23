from typing import List, Optional
from core.entities.film import Film
from core.repositories.film_repository import FilmRepository
from infrastructure.models.django_film import DjangoFilm


class DjangoFilmRepository(FilmRepository):
    def _to_entity(self, model: DjangoFilm) -> Film:
        return Film(
            id=model.id,
            title=model.title,
            episode_id=model.episode_id,
            opening_crawl=model.opening_crawl,
            director=model.director,
            producer=model.producer,
            release_date=str(model.release_date) if model.release_date else None,
            character_ids=list(model.characters.values_list('id', flat=True)),
            planet_ids=list(model.planets.values_list('id', flat=True))
        )

    def get_all(self) -> List[Film]:
        return [self._to_entity(f) for f in DjangoFilm.objects.prefetch_related('characters', 'planets')]

    def get_by_id(self, film_id: int) -> Optional[Film]:
        try:
            model = DjangoFilm.objects.prefetch_related('characters', 'planets').get(id=film_id)
            return self._to_entity(model)
        except DjangoFilm.DoesNotExist:
            return None

    def create(self, film: Film) -> Film:
        model = DjangoFilm.objects.create(
            title=film.title,
            episode_id=film.episode_id,
            opening_crawl=film.opening_crawl,
            director=film.director,
            producer=film.producer,
            release_date=film.release_date
        )
        if film.character_ids:
            model.characters.set(film.character_ids)
        if film.planet_ids:
            model.planets.set(film.planet_ids)
        return self._to_entity(model)

    def get_by_character_id(self, character_id: int) -> List[Film]:
        return [self._to_entity(f) for f in DjangoFilm.objects.filter(characters__id=character_id).prefetch_related('characters', 'planets')]

    def get_by_planet_id(self, planet_id: int) -> List[Film]:
        return [self._to_entity(f) for f in DjangoFilm.objects.filter(planets__id=planet_id).prefetch_related('characters', 'planets')]