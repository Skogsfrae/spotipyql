# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_artist_by_id 1'] = {
    'data': {
        'artist': {
            'genres': [
                'dark wave',
                'ethereal wave',
                'medieval folk',
                'neoclassical',
                'rune folk'
            ],
            'id': '5HwQ6LgbaJ9OifrTioZmRi',
            'name': 'Rajna',
            'popularity': 19,
            'type': 'artist',
            'uri': 'spotify:artist:5HwQ6LgbaJ9OifrTioZmRi'
        }
    }
}
