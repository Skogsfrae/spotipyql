# SpotipyQL [![Build Status](https://cloud.drone.io/api/badges/Skogsfrae/spotipyql/status.svg)](https://cloud.drone.io/Skogsfrae/spotipyql) ![Language](https://img.shields.io/github/languages/top/skogsfrae/spotipyql.svg?color=%2310101) ![License](https://img.shields.io/github/license/skogsfrae/spotipyql.svg?color=%2310101) ![Last commit](https://img.shields.io/github/last-commit/skogsfrae/spotipyql.svg?color=%2310101) 

GraphQL schema for Spotify Web Api written in Python 3

----

## On Docker

![](https://images.microbadger.com/badges/version/skogsfrae/spotipyql.svg) ![](https://images.microbadger.com/badges/image/skogsfrae/spotipyql.svg)

[![dockeri.co](https://dockeri.co/image/skogsfrae/spotipyql)](https://hub.docker.com/r/skogsfrae/spotipyql)

## Instructions

To try it out just 
1. clone the repo
2. install pipenv if you haven't already
3. run `pipenv install`
4. get your [spotify ids](https://developer.spotify.com)
5. run `pipenv shell`
6. export some env variables
```bash
export FLASK_APP='spotipyql'
export SPOTIPY_CLIENT_ID='your-client-id'
export SPOTIPY_CLIENT_SECRET='your-secret'
export SPOTIFY_SCOPES='user-read-private user-read-email'
```
7. run the server `flask run`

The server will run on http://localhost:5000.
The graphql api url will be http://localhost:5000/graphql exposed in POST method. If requested in GET from the browser, an interactive GraphQL ide will show up.
