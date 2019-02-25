from functools import wraps

from flask import Flask, g

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


def with_app_context(f):

  @wraps(f)
  def get_context(*args, **kwargs):
    app = Flask(__name__)
    app.config.from_object('spotipyql.env_config')

    with app.app_context():
      client_credentials_manager = SpotifyClientCredentials(
        client_id=app.config['SPOTIPY_CLIENT_ID'],
        client_secret=app.config['SPOTIPY_CLIENT_SECRET']
      )

      g.sp = Spotify(client_credentials_manager=client_credentials_manager)

      f(*args, **kwargs)

  return get_context