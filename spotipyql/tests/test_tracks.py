from graphene.test import Client

from spotipyql.schema import schema
from spotipyql.tests import utils


@utils.with_app_context
def test_get_track_by_id(snapshot):
  client = Client(schema)

  snapshot.assert_match(client.execute('''{
    track(id: "5HZZE1IYmIJAbrfKy6nO5v"){
      id
      name
      uri
      popularity
      discNumber
      durationMs
      explicit
      isPlayable
      previewUrl
      trackNumber
      type
      isLocal
      album{
        id
      }
      audioFeatures{
        id
        acousticness
        analysisUrl
        danceability
        durationMs
        energy
        instrumentalness
        key
        liveness
        loudness
        mode
        speechiness
        tempo
        timeSignature
        valence
      }
    }
  }'''))
