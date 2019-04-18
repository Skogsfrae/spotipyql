# SpotipyQL [![Build Status](https://cloud.drone.io/api/badges/Skogsfrae/spotipyql/status.svg)](https://cloud.drone.io/Skogsfrae/spotipyql) ![Language](https://img.shields.io/github/languages/top/skogsfrae/spotipyql.svg?color=%2310101&style=flat&logo=python) ![License](https://img.shields.io/github/license/skogsfrae/spotipyql.svg?color=%2310101) ![Last commit](https://img.shields.io/github/last-commit/skogsfrae/spotipyql.svg?color=%2310101&style=flat&logo=github) ![maintenance](https://img.shields.io/maintenance/yes/2019.svg)

GraphQL schema for Spotify Web Api written in Python 3

----

## On Docker

![](https://images.microbadger.com/badges/version/skogsfrae/spotipyql.svg) ![](https://images.microbadger.com/badges/image/skogsfrae/spotipyql.svg)

[![dockeri.co](https://dockeri.co/image/skogsfrae/spotipyql)](https://hub.docker.com/r/skogsfrae/spotipyql)

### Available env vars

`SPOTIPY_CLIENT_ID`

Your spotify client id

`SPOTIPY_CLIENT_SECRET`

Your spotify client secret

`SPOTIFY_SCOPES`

List of spotify api scopes white space separated

## Dev Instructions

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


# Api Coverage

List of [api endpoints](https://developer.spotify.com/documentation/web-api/reference/) coverage.

## Album
- [x] Get album from id
- [x] Get album tracks
- [ ] Get a list of albums

## Artist
- [x] Get artist from id
- [x] Get artist's albums
- [x] Get artist's top tracks
- [x] Get artist's related artists
- [ ] Get a list of artists

## Brows
- [ ] Get a category
- [ ] Get a category playlists
- [ ] Get a multiple categories
- [ ] Get a list of categories
- [ ] Get a list of featured playlists
- [ ] Get a list of new releases
- [ ] Get reccomendations based on seeds

## Follow
- [ ] Check if Current User Follows Artists or Users
- [ ] Check if Users Follow a Playlist
- [ ] Follow Artists or Users
- [ ] Follow a Playlist
- [ ] Get User's Followed Artists
- [ ] Unfollow Artists or Users
- [ ] Unfollow a Playlist

## Library
- [ ] Check User's Saved Albums
- [ ] Check User's Saved Tracks
- [ ] Get Current User's Saved Albums
- [ ] Get a User's Saved Tracks
- [ ] Remove Albums for Current User
- [ ] Remove User's Saved Tracks
- [ ] Save Albums for Current User
- [ ] Save Tracks for User	

## Personalization
- [ ] Get a User's Top Artists and Tracks

## Player
- [ ] Get a User's Available Devices
- [ ] Get Information About The User's Current Playback
- [ ] Get Current User's Recently Played Tracks
- [ ] Get the User's Currently Playing Track
- [ ] Pause a User's Playback
- [ ] Seek To Position In Currently Playing Track	
- [ ] Set Repeat Mode On User’s Playback
- [ ] Set Volume For User's Playback
- [ ] Skip User’s Playback To Next Track
- [ ] Skip User’s Playback To Previous Track
- [ ] Start/Resume a User's Playback	
- [ ] Toggle Shuffle For User’s Playback
- [ ] Transfer a User's Playback	

## Playlist
- [ ] Add Tracks to a Playlist
- [ ] Change a Playlist's Details
- [ ] Create a Playlist
- [x] Get a List of Current User's Playlists
- [x] Get a List of a User's Playlists
- [x] Get a Playlist Cover Image
- [ ] Get a Playlist
- [x] Get a Playlist's Tracks
- [ ] Remove Tracks from a Playlist	
- [ ] Reorder a Playlist's Tracks
- [ ] Replace a Playlist's Tracks
- [ ] Upload a Custom Playlist Cover Image

## Search
- [x] Generic Search

## Tracks
- [ ] Get Audio Analysis for a Track	
- [x] Get Audio Features for a Track
- [x] Get Audio Features for Several Tracks	
- [ ] Get Several Tracks
- [x] Get a Track

## Users Profile
- [x] Get Current User's Profile
- [x] Get a User's Profile	
