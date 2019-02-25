import os
from flask import Flask, request
from flask_graphql import GraphQLView

from spotipyql import auth
from spotipyql.schema.schema import schema


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('spotipyql.env_config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

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
