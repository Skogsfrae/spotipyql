from graphene.test import Client

from spotipyql.schema import schema
from spotipyql.tests import utils


@utils.with_app_context
def test_get_artist_by_id(snapshot):
  client = Client(schema)

  snapshot.assert_match(client.execute('''{
    artist(id: "5HwQ6LgbaJ9OifrTioZmRi"){
      id
      name
      uri
      popularity
      type
      genres
    }
  }'''))
