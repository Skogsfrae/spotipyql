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
            'discNumber': 1,
            'durationMs': 180826,
            'explicit': False,
            'id': '5HZZE1IYmIJAbrfKy6nO5v',
            'isLocal': 'false',
            'isPlayable': None,
            'name': 'Dreams Today',
            'popularity': 34,
            'previewUrl': 'https://p.scdn.co/mp3-preview/636b146cc6238523515178fd5102ddd651a033be?cid=5f7f9b9b2df043448b9bf03766fb36b0',
            'trackNumber': 8,
            'type': 'track',
            'uri': 'spotify:track:5HZZE1IYmIJAbrfKy6nO5v'
        }
    }
}
