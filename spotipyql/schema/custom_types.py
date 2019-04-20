from graphene import ObjectType, String

class SpotifyObject(ObjectType):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.api_data = kwargs


class SpotifyID(String):
  '''Spotify ID Scalar Type'''
  pass


class SpotifyUserID(String):
  '''Spotify ID Scalar Type'''
  pass
