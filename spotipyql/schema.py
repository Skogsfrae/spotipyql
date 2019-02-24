from datetime import datetime, date

import graphene
from graphene import Node, relay, Connection

from flask import g

from spotipyql.utils import filter_output


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

  @staticmethod
  def track_from_api(ApiData, album_id=None):
    data = filter_output(ApiData, Track.__dict__.keys())
    track = Track(**data)
    if 'album' in ApiData:
      track._album_id = ApiData['album']['id']
    elif album_id is not None:
      track._album_id = album_id
    return track

  def resolve_album(self, info, **args):
    if 'sp' in g:
      return Album.album_from_api(g.sp.album(self._album_id))


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

  @staticmethod
  def album_from_api(ApiData):
    data = filter_output(ApiData, Album.__dict__.keys())
    album = Album(**data)
    album._artists_ids = [i['id'] for i in data['artists']]
    return album

  def resolve_tracks(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.album_tracks(self.id)
      return [Track.track_from_api(track, self.id) for track in data['items']]
  
  def resolve_artists(self, info, **kwargs):
    if 'sp' in g:
      return [Artist.artist_from_api(g.sp.artist(i)) for i in self._artists_ids]


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

  @staticmethod
  def artist_from_api(ApiData):
    data = filter_output(ApiData, Artist.__dict__.keys())
    return Artist(**data)

  def resolve_albums(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.artist_albums(self.id)
      return [Album.album_from_api(album) for album in data['items']]
  
  def resolve_related_artists(self, info, **kwargs):
    if 'sp' in g:
      data = g.sp.artist_related_artists(self.id)
      return [Artist.artist_from_api(artist) for artist in data['artists']]

  def resolve_top_tracks(self, info, country='US', **kwargs):
    if 'sp' in g:
      data = g.sp.artist_top_tracks(self.id, country)
      return [Track.track_from_api(track) for track in data['tracks']]


class Query(graphene.ObjectType):
  artist = graphene.Field(Artist, id=graphene.String())
  album = graphene.Field(Album, id=graphene.String())
  track = graphene.Field(Track, id=graphene.String())
  
  def resolve_album(self, info, id):
    if 'sp' in g:
      return Album.album_from_api(g.sp.album(id))
  
  def resolve_track(self, info, id):
    if 'sp' in g:
      return Track.track_from_api(g.sp.track(id))
  
  def resolve_artist(self, info, id):
    if 'sp' in g:
      return Artist.artist_from_api(g.sp.artist(id))

schema = graphene.Schema(query=Query)