import pytest
from graphene.test import Client
from presentation.schema.schema import schema


@pytest.mark.django_db
class TestGraphQLQueries:
    def setup_method(self):
        self.client = Client(schema)

    def test_query_all_characters(self):
        query = '''
        query {
            allCharacters {
                edges {
                    node {
                        name
                    }
                }
            }
        }
        '''
        result = self.client.execute(query)
        assert 'errors' not in result
        assert 'allCharacters' in result['data']

    def test_query_characters_with_filter(self):
        query = '''
        query {
            characters(name: "Luke") {
                name
            }
        }
        '''
        result = self.client.execute(query)
        assert 'errors' not in result

    def test_query_planets(self):
        query = '''
        query {
            planets {
                name
                climate
            }
        }
        '''
        result = self.client.execute(query)
        assert 'errors' not in result


@pytest.mark.django_db
class TestGraphQLMutations:
    def setup_method(self):
        self.client = Client(schema)

    def test_create_character_mutation(self):
        mutation = '''
        mutation {
            createCharacter(name: "Chewbacca", height: "228", gender: "Masculino") {
                character {
                    id
                    name
                    height
                }
            }
        }
        '''
        result = self.client.execute(mutation)
        assert 'errors' not in result
        assert result['data']['createCharacter']['character']['name'] == "Chewbacca"

    def test_create_planet_mutation(self):
        mutation = '''
        mutation {
            createPlanet(name: "Mustafar", climate: "Caliente", terrain: "Volcánico") {
                planet {
                    id
                    name
                }
            }
        }
        '''
        result = self.client.execute(mutation)
        assert 'errors' not in result
        assert result['data']['createPlanet']['planet']['name'] == "Mustafar"