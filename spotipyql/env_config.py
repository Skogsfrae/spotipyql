import os

SECRET_KEY = os.environ.get("APP_SECRET", default='my-secret')

ENVIRONMENT_DEBUG = os.environ.get("DEBUG", default='False')
if ENVIRONMENT_DEBUG.lower() in ("f", "false"):
    ENVIRONMENT_DEBUG = False

DEBUG = ENVIRONMENT_DEBUG

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", default=False)
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", default=False)
SPOTIFY_SCOPES = os.environ.get("SPOTIFY_SCOPES", default=False)
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI", default=False)

