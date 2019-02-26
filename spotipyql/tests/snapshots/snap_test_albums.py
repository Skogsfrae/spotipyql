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
            'images': [
                {
                    'height': 640,
                    'url': 'https://i.scdn.co/image/19947c3fe5a54060721aebea0b552dabab2a5c32',
                    'width': 640
                },
                {
                    'height': 300,
                    'url': 'https://i.scdn.co/image/5e9a3b54eed85aa054e09476ce5263127f2ce622',
                    'width': 300
                },
                {
                    'height': 64,
                    'url': 'https://i.scdn.co/image/ab0ad0bae8cd20e50021c9d49f92c57f539c7ab3',
                    'width': 64
                }
            ],
            'label': 'Holy Records',
            'name': 'The Door Of Serenity',
            'popularity': 6,
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
