from graphene.test import Client

from spotipyql.schema import schema
from spotipyql.tests import utils


@utils.with_app_context
def test_get_public_user_by_id(snapshot):
  client = Client(schema)

  snapshot.assert_match(client.execute('''{
    publicUser(id: "skogsfrae"){
      id
      displayName
      images{
        url
        width
        height
      }
      type
      uri
      playlists(first: 1){
        id
        name
        collaborative
        images{
          url
          width
          height
        }
        owner{
          id
        }
        public
        snapshoId
        tracks{
          addedAt
          addedBy{
            id
          }
          isLocal
          track{
            id
            name
          }
        }
      }
    }
  }'''))
