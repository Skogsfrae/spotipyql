import graphene
from spotipyql.schema.media_schema import Query as MediaQuery
from spotipyql.schema.user_schema import Query as UserQuery
from spotipyql.schema.search_schema import Query as SearchQuery


class Query(MediaQuery, UserQuery, SearchQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)