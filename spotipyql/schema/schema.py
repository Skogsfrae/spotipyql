import graphene
from spotipyql.schema.media_schema import Query as MediaQuery


class Query(MediaQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)