import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from presentation.schema.types import CharacterType, PlanetType, FilmType
from infrastructure.models.django_character import DjangoCharacter
from infrastructure.models.django_planet import DjangoPlanet
from infrastructure.models.django_film import DjangoFilm


class Query(graphene.ObjectType):
    all_characters = DjangoFilterConnectionField(CharacterType)
    all_planets = DjangoFilterConnectionField(PlanetType)
    all_films = DjangoFilterConnectionField(FilmType)
    
    character = relay.Node.Field(CharacterType)
    planet = relay.Node.Field(PlanetType)
    film = relay.Node.Field(FilmType)
    
    characters = graphene.List(CharacterType, name=graphene.String(required=False))
    planets = graphene.List(PlanetType)
    films = graphene.List(FilmType)

    def resolve_all_characters(self, info, **kwargs):
        return DjangoCharacter.objects.all().prefetch_related('films', 'films__planets')

    def resolve_all_planets(self, info, **kwargs):
        return DjangoPlanet.objects.all().prefetch_related('films')

    def resolve_all_films(self, info, **kwargs):
        return DjangoFilm.objects.all().prefetch_related('characters', 'planets')

    def resolve_characters(self, info, name=None):
        queryset = DjangoCharacter.objects.all().prefetch_related('films', 'films__planets')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def resolve_planets(self, info):
        return DjangoPlanet.objects.all().prefetch_related('films')

    def resolve_films(self, info):
        return DjangoFilm.objects.all().prefetch_related('characters', 'planets')