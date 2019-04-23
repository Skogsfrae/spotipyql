from flask_oauthlib.client import OAuthException

class SpotifyClient(object):
  def __init__(self, oauth_client, *args, **kwargs):
    self.base_url = 'https://api.spotify.com/v1'
    self.spotify = oauth_client

  def _get(self, url, data=None):
    data = self.spotify.get(url, data=data)
    if data.status is not 200:
      msg = ''
      if 'error' in data.data.keys():
        msg = data.data['error']['message']
      else:
        msg = data._resp.msg
      raise OAuthException(msg)
    
    return data.data

  def me(self):
    return self._get('/v1/me')

  def users(self, user_id):
    return self._get('/v1/users/{user_id}'.format(**{
      'user_id': user_id
    }))

  '''
  Albums
  '''
  def album(self, id):
    return self._get('/v1/albums/{album_id}'.format(**{
      'album_id': id
    }))

  def album_track(self, album_id):
    return self._get('/v1/albums/{album_id}/tracks'.format(**{
      'id': id
    }))

  '''
  Artists
  '''
  def artist(self, id):
    return self._get('/v1/artists/{artist_id}'.format(**{
      'artist_id': id
    }))

  def artist_albums(self, id):
    return self._get('/v1/artists/{artist_id}/albums'.format(**{
      'artist_id': id
    }))

  def artist_top_tracks(self, id):
    return self._get('/v1/artists/{artist_id}/top-tracks'.format(**{
      'artist_id': id
    }))

  def artist_related_artists(self, id):
    return self._get('/v1/artists/{artist_id}/related-artists'.format(**{
      'artist_id': id
    }))

  '''
  Tracks
  '''
  def track(self, id):
    return self._get('/v1/tracks/{track_id}'.format(**{
      'track_id': id
    }))

  def track_audio_features(self, id):
    return self._get('/v1/audio-features/{track_id}'.format(**{
      'track_id': id
    }))

  def track_audio_analysis(self, id):
    return self._get('/v1/audio-analysis/{track_id}'.format(**{
      'track_id': id
    }))

  '''
  Search
  '''
  def search(self, q, type, limit, offset):
    return self._get('/v1/search', data={
      'q': q,
      'type': type,
      'limit': limit,
      'offset': offset
    })

  def devices(self):
    return self._get('/v1/me/player/devices')

