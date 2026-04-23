from infrastructure.models.django_film import DjangoFilm
from infrastructure.models.django_character import DjangoCharacter
from infrastructure.models.django_planet import DjangoPlanet


def load_initial_data():
    pelicula1, _ = DjangoFilm.objects.get_or_create(
        title="Una Nueva Esperanza",
        defaults={
            'episode_id': 4,
            'opening_crawl': "Es un período de guerra civil. Naves espaciales rebeldes, atacando desde una base oculta, han logrado su primera victoria contra el malvado Imperio Galáctico...",
            'director': "George Lucas",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1977-05-25"
        }
    )

    pelicula2, _ = DjangoFilm.objects.get_or_create(
        title="El Imperio Contraataca",
        defaults={
            'episode_id': 5,
            'opening_crawl': "Es una época oscura para la Rebelión. Aunque la Estrella de la Muerte ha sido destruida, las tropas imperiales han expulsado a las fuerzas rebeldes de sus bases ocultas y las persiguen por toda la galaxia...",
            'director': "Irvin Kershner",
            'producer': "Gary Kurtz, Rick McCallum",
            'release_date': "1980-05-21"
        }
    )

    pelicula3, _ = DjangoFilm.objects.get_or_create(
        title="El Retorno del Jedi",
        defaults={
            'episode_id': 6,
            'opening_crawl': "Luke Skywalker ha regresado a Tatooine, su planeta natal, para intentar rescatar a su amigo Han Solo de las garras del malvado Jabba el Hutt...",
            'director': "Richard Marquand",
            'producer': "Howard Kazanjian, George Lucas, Rick McCallum",
            'release_date': "1983-05-25"
        }
    )

    planeta1, _ = DjangoPlanet.objects.get_or_create(
        name="Tatooine",
        defaults={
            'climate': "Árido",
            'terrain': "Desierto",
            'population': "200000",
            'gravity': "1 estándar",
            'diameter': "10465"
        }
    )

    planeta2, _ = DjangoPlanet.objects.get_or_create(
        name="Alderaan",
        defaults={
            'climate': "Templado",
            'terrain': "Praderas, Montañas",
            'population': "2000000000",
            'gravity': "1 estándar",
            'diameter': "12500"
        }
    )

    planeta3, _ = DjangoPlanet.objects.get_or_create(
        name="Dagobah",
        defaults={
            'climate': "Húmedo",
            'terrain': "Pantano, Jungla",
            'population': "Desconocida",
            'gravity': "0.9 estándar",
            'diameter': "8900"
        }
    )

    planeta4, _ = DjangoPlanet.objects.get_or_create(
        name="Hoth",
        defaults={
            'climate': "Congelado",
            'terrain': "Tundra, Cuevas de hielo, Montañas",
            'population': "Desconocida",
            'gravity': "1.1 estándar",
            'diameter': "7200"
        }
    )

    luke, _ = DjangoCharacter.objects.get_or_create(
        name="Luke Skywalker",
        defaults={
            'height': "172",
            'mass': "77",
            'hair_color': "Rubio",
            'skin_color': "Claro",
            'eye_color': "Azul",
            'birth_year': "19 ABY",
            'gender': "Masculino"
        }
    )

    leia, _ = DjangoCharacter.objects.get_or_create(
        name="Leia Organa",
        defaults={
            'height': "150",
            'mass': "49",
            'hair_color': "Castaño",
            'skin_color': "Claro",
            'eye_color': "Castaño",
            'birth_year': "19 ABY",
            'gender': "Femenino"
        }
    )

    han, _ = DjangoCharacter.objects.get_or_create(
        name="Han Solo",
        defaults={
            'height': "180",
            'mass': "80",
            'hair_color': "Castaño",
            'skin_color': "Claro",
            'eye_color': "Marrón",
            'birth_year': "29 ABY",
            'gender': "Masculino"
        }
    )

    vader, _ = DjangoCharacter.objects.get_or_create(
        name="Darth Vader",
        defaults={
            'height': "202",
            'mass': "136",
            'hair_color': "Ninguno",
            'skin_color': "Blanco",
            'eye_color': "Amarillo",
            'birth_year': "41 ABY",
            'gender': "Masculino"
        }
    )

    yoda, _ = DjangoCharacter.objects.get_or_create(
        name="Yoda",
        defaults={
            'height': "66",
            'mass': "13",
            'hair_color': "Blanco",
            'skin_color': "Verde",
            'eye_color': "Marrón",
            'birth_year': "896 ABY",
            'gender': "Masculino"
        }
    )

    luke.films.add(pelicula1, pelicula2, pelicula3)
    leia.films.add(pelicula1, pelicula2, pelicula3)
    han.films.add(pelicula1, pelicula2, pelicula3)
    vader.films.add(pelicula1, pelicula2, pelicula3)
    yoda.films.add(pelicula2, pelicula3)

    pelicula1.planets.add(planeta1, planeta2)
    pelicula2.planets.add(planeta1, planeta3, planeta4)
    pelicula3.planets.add(planeta1, planeta4)

    print("Datos iniciales cargados correctamente")