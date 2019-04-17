# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_track_by_id 1'] = {
    'data': {
        'track': {
            'album': {
                'id': '6IsCOalvnAxZbDseDoG1ep'
            },
            'audioFeatures': {
                'acousticness': 0.948,
                'analysisUrl': 'https://api.spotify.com/v1/audio-analysis/5HZZE1IYmIJAbrfKy6nO5v',
                'danceability': 0.525,
                'durationMs': 180827,
                'energy': 0.37,
                'id': '5HZZE1IYmIJAbrfKy6nO5v',
                'instrumentalness': 0.894,
                'key': 11,
                'liveness': 0.0864,
                'loudness': -17.447,
                'mode': 1,
                'speechiness': 0.0413,
                'tempo': 175.934,
                'timeSignature': 4,
                'valence': 0.294
            },
            'discNumber': 1,
            'durationMs': 180826,
            'explicit': False,
            'id': '5HZZE1IYmIJAbrfKy6nO5v',
            'isLocal': 'false',
            'isPlayable': None,
            'name': 'Dreams Today',
            'popularity': 36,
            'previewUrl': 'https://p.scdn.co/mp3-preview/636b146cc6238523515178fd5102ddd651a033be?cid=5f7f9b9b2df043448b9bf03766fb36b0',
            'trackNumber': 8,
            'type': 'track',
            'uri': 'spotify:track:5HZZE1IYmIJAbrfKy6nO5v'
        }
    }
}
