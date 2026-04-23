from typing import List, Optional
from core.entities.planet import Planet
from core.repositories.planet_repository import PlanetRepository
from infrastructure.models.django_planet import DjangoPlanet


class DjangoPlanetRepository(PlanetRepository):
    def _to_entity(self, model: DjangoPlanet) -> Planet:
        return Planet(
            id=model.id,
            name=model.name,
            climate=model.climate,
            terrain=model.terrain,
            population=model.population,
            gravity=model.gravity,
            diameter=model.diameter
        )

    def get_all(self) -> List[Planet]:
        return [self._to_entity(p) for p in DjangoPlanet.objects.all()]

    def get_by_id(self, planet_id: int) -> Optional[Planet]:
        try:
            model = DjangoPlanet.objects.get(id=planet_id)
            return self._to_entity(model)
        except DjangoPlanet.DoesNotExist:
            return None

    def create(self, planet: Planet) -> Planet:
        model = DjangoPlanet.objects.create(
            name=planet.name,
            climate=planet.climate,
            terrain=planet.terrain,
            population=planet.population,
            gravity=planet.gravity,
            diameter=planet.diameter
        )
        return self._to_entity(model)