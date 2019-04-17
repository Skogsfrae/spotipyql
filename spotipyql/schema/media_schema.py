from datetime import datetime, date

import graphene

from flask import g

from spotipyql.utils import filter_output
import spotipyql.schema.misc_schema as misc_schema

class Track(graphene.ObjectType):
  id = graphene.String()
  name = graphene.String()
  uri = graphene.String()
  popularity = graphene.Int()
  disc_number = graphene.Int()
  duration_ms = graphene.Int()
  explicit = graphene.Boolean()
  is_playable = graphene.Boolean()
  preview_url = graphene.String()
  track_number = graphene.Int()
  type = graphene.String()
  is_local = graphene.String()
  album = graphene.Field(lambda: Album)
  audioFeatures = graphene.Field(lambda: AudioFeatures)

  @staticmethod
  def from_api(ApiData, album_id=None):
    data = filter_output(ApiData, Track.__dict__.keys())
    track = Track(**data)
    if 'album' in ApiData:
      track._album_id = ApiData['album']['id']
    elif album_id is not None:
      track._album_id = album_id
    return track

  def resolve_album(self, info, **args):
    if 'sp' in g:
      return Album.from_api(g.sp.album(self._album_id))

  def resolve_audioFeatures(self, info, **kwargs):
    if 'sp' in g:
      return AudioFeatures.from_api(g.sp.audio_features([self.id]))

class Album(graphene.ObjectType):
  id = graphene.String()
  name = graphene.String()
  uri = graphene.String()
  popularity = graphene.Int()
  genres = graphene.List(graphene.String)
  label = graphene.String()
  album_type = graphene.String()
  release_date = graphene.String()
  total_traks = graphene.Int()
  type = graphene.String()
  tracks = graphene.List(lambda: Track)
  artists = graphene.List(lambda: Artist)
  images = graphene.List(lambda: misc_schema.Image)

  @staticmethod
  def from_api(ApiData):
    data = filter_output(ApiData, Album.__dict__.keys())
    album = Album(**data)
    album._artists_ids = [i['id'] for i in data['artists']]
    album.images = [misc_schema.Image(**img) for img in data['images']]
    return album

  def resolve_tracks(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.album_tracks(self.id)
      return [Track.from_api(track, self.id) for track in data['items']]
  
  def resolve_artists(self, info, **kwargs):
    if 'sp' in g:
      return [Artist.from_api(g.sp.artist(i)) for i in self._artists_ids]


class Artist(graphene.ObjectType):
  id = graphene.String()
  name = graphene.String()
  uri = graphene.String()
  popularity = graphene.Int()
  genres = graphene.List(graphene.String)
  type = graphene.String()
  albums = graphene.List(lambda: Album)
  related_artists = graphene.List(lambda: Artist)
  top_tracks = graphene.List(lambda: Track, country=graphene.String())
  images = graphene.List(lambda: misc_schema.Image)

  @staticmethod
  def from_api(ApiData):
    data = filter_output(ApiData, Artist.__dict__.keys())
    artist = Artist(**data)
    artist.images = [misc_schema.Image(**img) for img in data['images']]
    return artist

  def resolve_albums(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.artist_albums(self.id)
      return [Album.from_api(album) for album in data['items']]
  
  def resolve_related_artists(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.artist_related_artists(self.id)
      return [Artist.from_api(artist) for artist in data['artists']]

  def resolve_top_tracks(self, info, country='US', **kwargs):
    if 'sp' in g:
      data = g.sp.artist_top_tracks(self.id, country)
      return [Track.from_api(track) for track in data['tracks']]


class AudioFeatures(graphene.ObjectType):
  id = graphene.String()
  acousticness = graphene.Float()
  analysis_url = graphene.String()
  danceability = graphene.Float()
  duration_ms = graphene.Int()
  energy = graphene.Float()
  instrumentalness = graphene.Float()
  key = graphene.Int() # convert to enumeration
  liveness = graphene.Float()
  loudness = graphene.Float()
  mode = graphene.Int() # convert to enumeration
  speechiness = graphene.Float()
  tempo = graphene.Float()
  time_signature = graphene.Int()
  valence = graphene.Float()
  track = graphene.Field(lambda: Track)

  @staticmethod
  def from_api(ApiData):
    data = filter_output(ApiData[0], AudioFeatures.__dict__.keys())
    aFeat = AudioFeatures(**data)
    return aFeat

  def resolve_track(self, info, **kwargs):
    if 'sp' in g:
      return Track.from_api(g.sp.track(self.id))


class Query(object):
  artist = graphene.Field(Artist, id=graphene.String())
  album = graphene.Field(Album, id=graphene.String())
  track = graphene.Field(Track, id=graphene.String())
  audioFeatures = graphene.List(AudioFeatures, trackIds=graphene.List(graphene.String))
  
  def resolve_album(self, info, id):
    if 'sp' in g:
      return Album.from_api(g.sp.album(id))
  
  def resolve_track(self, info, id):
    if 'sp' in g:
      return Track.from_api(g.sp.track(id))
  
  def resolve_artist(self, info, id):
    if 'sp' in g:
      return Artist.from_api(g.sp.artist(id))
  
  def resolve_audioFeatures(self, info, trackIds):
    if 'sp' in g:
      return [AudioFeatures.from_api(g.sp.audio_features(id)) for id in trackIds]