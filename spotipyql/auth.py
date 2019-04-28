from functools import wraps
from flask import Flask, session, redirect, request, Blueprint, current_app, abort, url_for, g
from flask_oauthlib.client import OAuth, OAuthException

from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from spotipy import Spotify
from spotipyql.rest_client.client import SpotifyClient


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET'])
def authenticate():
  cb = url_for('auth.callback',
                _external=True)
  return current_app.spotify.authorize(callback=cb)


@bp.route('/callback', methods=['GET'])
def callback():
  if request.args.get('error', False):
    return abort(401)

  try:
    resp = current_app.spotify.authorized_response()
  except OAuthException as e:
    return e

  if resp is None:
    return 'Access denied: reason={0} error={1}'.format(
        request.args['error_reason'],
        request.args['error_description']
    )
  
  if isinstance(resp, OAuthException):
    return 'Access denied: {0}'.format(resp.message)
  
  # code = request.args.get('code', '')
  # token = g.soa.get_access_token(code)
  session['token'] = resp.get('access_token', '')

  return redirect(url_for('graphql'))


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            return redirect(url_for('auth.authenticate'))

        # TODO: test if this works properly or if it rather uses the same Spotify
        # instance for each call
        if 'sp' not in g:
          g.sp = SpotifyClient(oauth_client=current_app.spotify)

        if 'soa' not in g:
          g.soa = current_app.spotify
          
        # if g.soa._is_token_expired(session['token']):
          # session['token'] = g.soa.refresh_access_token(session['token']['refresh_token'])
          #return redirect(url_for('auth.authenticate'))
        
        return f(*args, **kwargs)
    return decorated_function