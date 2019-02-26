import graphene

from flask import g

from spotipyql.utils import filter_output
import spotipyql.schema.playlist_schema as playlist_schema
import spotipyql.schema.media_schema as media_schema


class SearchResults(graphene.Union):
  class Meta:
    types = (playlist_schema.Playlist,
              media_schema.Album,
              media_schema.Artist,
              media_schema.Track
            )

class Query(object):
  search = graphene.List(
    SearchResults,
    q=graphene.String(),
    types=graphene.String(),
    first=graphene.Int(),
    offset=graphene.Int()
  )

  def resolve_search(self, info, q, types="playlist,album,artist,track", first=10, offset=0, **kwargs):
    if 'sp' in g:
      data = g.sp.search(q, type=types, limit=first, offset=offset)
      albums = [media_schema.Album.from_api(a) for a in data['albums']['items']]
      artists = [media_schema.Artist.from_api(a) for a in data['artists']['items']]
      tracks = [media_schema.Track.from_api(a) for a in data['tracks']['items']]
      playlists = [playlist_schema.Playlist.from_api(a) for a in data['playlists']['items']]
      return albums + artists + tracks + playlists