import graphene
from presentation.schema.types import CharacterType, PlanetType, FilmType
from infrastructure.models.django_character import DjangoCharacter
from infrastructure.models.django_planet import DjangoPlanet
from infrastructure.models.django_film import DjangoFilm


class CreateCharacter(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        film_ids = graphene.List(graphene.Int)

    character = graphene.Field(CharacterType)

    def mutate(self, info, name, height=None, mass=None, hair_color=None, skin_color=None, eye_color=None, birth_year=None, gender=None, film_ids=None):
        character = DjangoCharacter.objects.create(
            name=name,
            height=height,
            mass=mass,
            hair_color=hair_color,
            skin_color=skin_color,
            eye_color=eye_color,
            birth_year=birth_year,
            gender=gender
        )
        if film_ids:
            character.films.set(film_ids)
        return CreateCharacter(character=character)


class CreatePlanet(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        climate = graphene.String()
        terrain = graphene.String()
        population = graphene.String()
        gravity = graphene.String()
        diameter = graphene.String()

    planet = graphene.Field(PlanetType)

    def mutate(self, info, name, climate=None, terrain=None, population=None, gravity=None, diameter=None):
        planet = DjangoPlanet.objects.create(
            name=name,
            climate=climate,
            terrain=terrain,
            population=population,
            gravity=gravity,
            diameter=diameter
        )
        return CreatePlanet(planet=planet)


class CreateFilm(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        episode_id = graphene.Int()
        opening_crawl = graphene.String()
        director = graphene.String()
        producer = graphene.String()
        release_date = graphene.String()
        character_ids = graphene.List(graphene.Int)
        planet_ids = graphene.List(graphene.Int)

    film = graphene.Field(FilmType)

    def mutate(self, info, title, episode_id=None, opening_crawl=None, director=None, producer=None, release_date=None, character_ids=None, planet_ids=None):
        film = DjangoFilm.objects.create(
            title=title,
            episode_id=episode_id,
            opening_crawl=opening_crawl,
            director=director,
            producer=producer,
            release_date=release_date
        )
        if character_ids:
            film.characters.set(character_ids)
        if planet_ids:
            film.planets.set(planet_ids)
        return CreateFilm(film=film)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    create_planet = CreatePlanet.Field()
    create_film = CreateFilm.Field()