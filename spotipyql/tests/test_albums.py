from graphene.test import Client

from spotipyql.schema import schema
from spotipyql.tests import utils


@utils.with_app_context
def test_get_album_by_id(snapshot):
  client = Client(schema)

  snapshot.assert_match(client.execute('''{
    album(id: "6zAFtprBsbpQDUcVTzhUoA"){
      id
      name
      uri
      popularity
      type
      genres
      label
      albumType
      releaseDate
      totalTraks
      tracks{
        id
      }
      artists{
        id
      }
    }
  }'''))
