# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_album_by_id 1'] = {
    'data': {
        'album': {
            'albumType': 'album',
            'artists': [
                {
                    'id': '5HwQ6LgbaJ9OifrTioZmRi'
                }
            ],
            'genres': [
            ],
            'id': '6zAFtprBsbpQDUcVTzhUoA',
            'label': 'Holy Records',
            'name': 'The Door Of Serenity',
            'popularity': 5,
            'releaseDate': '2008-07-07',
            'totalTraks': None,
            'tracks': [
                {
                    'id': '5n8JX9kPWk7JJrL2MPlcEm'
                },
                {
                    'id': '5s9rmyfIB03EF8kYSVptFM'
                },
                {
                    'id': '60o3E8A7kzD0ABKobbsQ96'
                },
                {
                    'id': '20caoRjgdbJdbu8I7DHK24'
                },
                {
                    'id': '4opwBTg3yAoktng5NtOAZj'
                },
                {
                    'id': '5Ko5xkeoJOehyErcHXNjwg'
                },
                {
                    'id': '6LHwIiUUnNUdYdyIAEne0q'
                },
                {
                    'id': '1tEN1bmirgQBfsM5GaquNX'
                },
                {
                    'id': '2HTNsMM3RlQatlnZrGja5l'
                },
                {
                    'id': '4rfALAjBn7JaCqNlJOS5eD'
                },
                {
                    'id': '1gnk4MdhzgE8LxnXF8ocRF'
                },
                {
                    'id': '0JKptvKccgHTM3n0ujdJLY'
                }
            ],
            'type': 'album',
            'uri': 'spotify:album:6zAFtprBsbpQDUcVTzhUoA'
        }
    }
}
