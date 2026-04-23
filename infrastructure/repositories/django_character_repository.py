from typing import List, Optional
from django.db.models import Q
from core.entities.character import Character
from core.repositories.character_repository import CharacterRepository
from infrastructure.models.django_character import DjangoCharacter


class DjangoCharacterRepository(CharacterRepository):
    def _to_entity(self, model: DjangoCharacter) -> Character:
        return Character(
            id=model.id,
            name=model.name,
            height=model.height,
            mass=model.mass,
            hair_color=model.hair_color,
            skin_color=model.skin_color,
            eye_color=model.eye_color,
            birth_year=model.birth_year,
            gender=model.gender,
            film_ids=list(model.films.values_list('id', flat=True))
        )

    def get_all(self, name_filter: Optional[str] = None) -> List[Character]:
        queryset = DjangoCharacter.objects.all()
        if name_filter:
            queryset = queryset.filter(Q(name__icontains=name_filter))
        return [self._to_entity(c) for c in queryset.prefetch_related('films')]

    def get_by_id(self, character_id: int) -> Optional[Character]:
        try:
            model = DjangoCharacter.objects.prefetch_related('films').get(id=character_id)
            return self._to_entity(model)
        except DjangoCharacter.DoesNotExist:
            return None

    def create(self, character: Character) -> Character:
        model = DjangoCharacter.objects.create(
            name=character.name,
            height=character.height,
            mass=character.mass,
            hair_color=character.hair_color,
            skin_color=character.skin_color,
            eye_color=character.eye_color,
            birth_year=character.birth_year,
            gender=character.gender
        )
        if character.film_ids:
            model.films.set(character.film_ids)
        return self._to_entity(model)