# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_artist_by_id 1'] = {
    'data': {
        'artist': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 5,
                    'line': 2
                }
            ],
            'message': '''http status: 404, code:-1 - https://api.spotify.com/v1/artists/6zAFtprBsbpQDUcVTzhUoA:
 non existing id''',
            'path': [
                'artist'
            ]
        }
    ]
}
