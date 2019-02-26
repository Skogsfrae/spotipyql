import graphene

from flask import g

from spotipyql.utils import filter_output
import spotipyql.schema.media_schema as media_schema
import spotipyql.schema.user_schema as user_schema
import spotipyql.schema.misc_schema as misc_schema


class PlaylistTrack(graphene.ObjectType):
  added_at = graphene.DateTime()
  added_by = graphene.Field(lambda: user_schema.PublicUser)
  is_local = graphene.Boolean()
  # primary_color = graphene.?????
  track = graphene.Field(lambda: media_schema.Track)

  @staticmethod
  def from_api(ApiData, publicUser):
    data = filter_output(ApiData, PlaylistTrack.__dict__.keys())
    playlistTrack = PlaylistTrack(**data)
    playlistTrack.added_by = publicUser
    track_data = filter_output(data['track'], media_schema.Track.__dict__.keys())
    playlistTrack.track = media_schema.Track(**track_data)
    return playlistTrack


class Playlist(graphene.ObjectType):
  id = graphene.String()
  name = graphene.String()
  collaborative = graphene.Boolean()
  images = graphene.List(lambda: misc_schema.Image)
  owner = graphene.Field(lambda: user_schema.PublicUser)
  public = graphene.Boolean()
  snapsho_id = graphene.String()
  tracks = graphene.List(lambda: PlaylistTrack, first=graphene.Int(), offset=graphene.Int())
  type = graphene.String()
  uri = graphene.String()

  @staticmethod
  def from_api(ApiData, publicUser=None):
    data = filter_output(ApiData, Playlist.__dict__.keys())
    playlist = Playlist(**data)
    playlist.images = [misc_schema.Image(**img) for img in data['images']]
    if publicUser:
      playlist.owner = publicUser
    else:
      playlist.owner = user_schema.PublicUser.from_api(data['owner'])
    return playlist

  def resolve_tracks(self, info, first=100, offset=0):
    if 'sp' in g:
      data = g.sp.user_playlist_tracks(self.owner.id, self.id, limit=first, offset=offset)
      return [PlaylistTrack.from_api(t, self.owner) for t in data['items']]
