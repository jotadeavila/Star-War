import graphene
from presentation.schema.queries import Query
from presentation.schema.mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)