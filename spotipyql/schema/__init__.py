import graphene
from spotipyql.schema.media_schema import Query as MediaQuery
from spotipyql.schema.user_schema import Query as UserQuery


class Query(MediaQuery, UserQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)