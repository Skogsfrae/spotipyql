# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_public_user_by_id 1'] = {
    'data': {
        'publicUser': {
            'displayName': 'Mirko Mucaria',
            'id': 'skogsfrae',
            'images': [
                {
                    'height': None,
                    'url': None,
                    'width': None
                }
            ],
            'playlists': [
                {
                    'collaborative': False,
                    'id': '2h2VwQgagkSlRuOZ7wr9PT',
                    'images': [
                        {
                            'height': 640,
                            'url': 'https://mosaic.scdn.co/640/0e9990ef32fca7be395655b0f58ac587623f671f213645b0e652330dfc25f0f482a0af4aac9490b97118310c7af3fc8a92362a4e884e3d3ff78fe248aab96a64e5948f2cfca00455f89ccab88bb4b1fb',
                            'width': 640
                        },
                        {
                            'height': 300,
                            'url': 'https://mosaic.scdn.co/300/0e9990ef32fca7be395655b0f58ac587623f671f213645b0e652330dfc25f0f482a0af4aac9490b97118310c7af3fc8a92362a4e884e3d3ff78fe248aab96a64e5948f2cfca00455f89ccab88bb4b1fb',
                            'width': 300
                        },
                        {
                            'height': 60,
                            'url': 'https://mosaic.scdn.co/60/0e9990ef32fca7be395655b0f58ac587623f671f213645b0e652330dfc25f0f482a0af4aac9490b97118310c7af3fc8a92362a4e884e3d3ff78fe248aab96a64e5948f2cfca00455f89ccab88bb4b1fb',
                            'width': 60
                        }
                    ],
                    'name': 'Test SpotipyQL',
                    'owner': {
                        'id': 'skogsfrae'
                    },
                    'public': True,
                    'snapshoId': None,
                    'tracks': [
                        {
                            'addedAt': '2019-03-03T22:12:47+00:00',
                            'addedBy': {
                                'id': 'skogsfrae'
                            },
                            'isLocal': False,
                            'track': {
                                'id': '4XGE9yJiHjbCAZ3L281daZ',
                                'name': 'Black Summer'
                            }
                        },
                        {
                            'addedAt': '2019-03-03T22:12:52+00:00',
                            'addedBy': {
                                'id': 'skogsfrae'
                            },
                            'isLocal': False,
                            'track': {
                                'id': '15qTaLMeTJCPfebHHzDdL0',
                                'name': 'Ice and the Storm'
                            }
                        },
                        {
                            'addedAt': '2019-03-03T22:12:55+00:00',
                            'addedBy': {
                                'id': 'skogsfrae'
                            },
                            'isLocal': False,
                            'track': {
                                'id': '35iW2nbKzxanlcC8dExP8W',
                                'name': 'Goneja'
                            }
                        },
                        {
                            'addedAt': '2019-03-03T22:13:01+00:00',
                            'addedBy': {
                                'id': 'skogsfrae'
                            },
                            'isLocal': False,
                            'track': {
                                'id': '6z7ZTqga3zgWBkREod45j0',
                                'name': 'Apayrı'
                            }
                        },
                        {
                            'addedAt': '2019-03-03T22:13:09+00:00',
                            'addedBy': {
                                'id': 'skogsfrae'
                            },
                            'isLocal': False,
                            'track': {
                                'id': '2lCzK9Ok3pyfFBsXgElpQl',
                                'name': 'Kedi Gibi'
                            }
                        }
                    ]
                }
            ],
            'type': 'PublicUser',
            'uri': 'spotify:user:skogsfrae'
        }
    }
}
