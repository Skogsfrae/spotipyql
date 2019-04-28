import os
from flask import Flask, request, g, session
from flask_graphql import GraphQLView
from flask_oauthlib.client import OAuth

from spotipyql import auth
from spotipyql.schema import schema
from spotipyql.cache import cache
from spotipyql import env_config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cache.init_app(app)
    oauth = OAuth(app)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('spotipyql.env_config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    spotify = oauth.remote_app(
                        'spotify',
                        consumer_key = app.config['SPOTIPY_CLIENT_ID'],
                        consumer_secret = app.config['SPOTIPY_CLIENT_SECRET'],
                        base_url = 'https://api.spotify.com',
                        request_token_url = None,
                        access_token_url = 'https://accounts.spotify.com/api/token',
                        authorize_url='https://accounts.spotify.com/authorize',
                        request_token_params = {'scope' : app.config['SPOTIFY_SCOPES']}
                    )
    app.spotify = spotify

    @spotify.tokengetter
    def tokengetter(token=None):
        return session.get('token', None)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)

    app.add_url_rule(
        '/graphql',
        view_func=auth.auth_required(GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True # for having the GraphiQL interface
        ))
    )

    return app
