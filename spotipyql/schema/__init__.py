import graphene
from spotipyql.schema.media_schema import Query as MediaQuery
from spotipyql.schema.user_schema import Query as UserQuery
from spotipyql.schema.search_schema import Query as SearchQuery
from spotipyql.schema.player_schema import Query as PlayerQuery


class Query(MediaQuery, UserQuery, SearchQuery, PlayerQuery, graphene.ObjectType):
  pass

schema = graphene.Schema(query=Query)