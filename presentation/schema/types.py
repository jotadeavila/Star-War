import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from infrastructure.models.django_character import DjangoCharacter
from infrastructure.models.django_planet import DjangoPlanet
from infrastructure.models.django_film import DjangoFilm


class PlanetType(DjangoObjectType):
    class Meta:
        model = DjangoPlanet
        fields = ('id', 'name', 'climate', 'terrain', 'population', 'gravity', 'diameter', 'films')
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class FilmType(DjangoObjectType):
    characters_direct = graphene.List(lambda: CharacterType)
    planets_direct = graphene.List(PlanetType)
    
    class Meta:
        model = DjangoFilm
        fields = ('id', 'title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'characters', 'planets')
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
    
    def resolve_characters_direct(self, info):
        return self.characters.all()
    
    def resolve_planets_direct(self, info):
        return self.planets.all()


class CharacterType(DjangoObjectType):
    films_direct = graphene.List(FilmType)
    
    class Meta:
        model = DjangoCharacter
        fields = ('id', 'name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'films')
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
    
    def resolve_films_direct(self, info):
        return self.films.all()