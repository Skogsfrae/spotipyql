from functools import wraps
from flask import Flask, session, redirect, request, Blueprint, current_app, abort, url_for, g
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotipy import Spotify


bp = Blueprint('auth', __name__, url_prefix='/auth')
def soa():
  return SpotifyOAuth(
    current_app.config['SPOTIPY_CLIENT_ID'],
    current_app.config['SPOTIPY_CLIENT_SECRET'],
    url_for('auth.callback', _external=True),
    scope=current_app.config['SPOTIFY_SCOPES']
  )

@bp.route('/login', methods=['GET'])
def authenticate():
  if 'soa' not in g:
    g.soa = soa()
  return redirect(g.soa.get_authorize_url())


@bp.route('/callback', methods=['GET'])
def callback():
  if request.args.get('error', False):
    return abort(401)
  
  if 'soa' not in g:
    g.soa = soa()
  
  code = request.args.get('code', '')
  token = g.soa.get_access_token(code)
  session['token'] = token

  return redirect(url_for('graphql'))


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            return redirect(url_for('auth.authenticate'))

        # TODO: test if this works properly or if it rather uses the same Spotify
        # instance for each call
        if 'sp' not in g:
          g.sp = Spotify(session['token']['access_token'])

        if 'soa' not in g:
          g.soa = soa()
          
        if g.soa._is_token_expired(session['token']):
          session['token'] = g.soa.refresh_access_token(session['token']['refresh_token'])
          #return redirect(url_for('auth.authenticate'))
        
        return f(*args, **kwargs)
    return decorated_function