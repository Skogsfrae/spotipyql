from datetime import datetime, date

import graphene

from flask import g

from spotipyql.utils import filter_output
from spotipyql.schema.custom_types import SpotifyObject, SpotifyID


class DeviceType(graphene.Enum):
  COMPUTER = 'Computer'
  TABLET = 'Tablet'
  SMARTPHONE = 'Smartphone'
  SPEAKER = 'Speaker'
  TV = 'TV'
  AVR = 'AVR'
  STB = 'STB'
  AUDIODONGLE = 'AudioDongle'
  GAMECONSOLE = 'GameConsole'
  CASTVIDEO = 'CastVideo'
  CASTAUDIO = 'CastAudio'
  AUTOMOBILE = 'Automobile'
  UNKNOWN = 'Unknown'

class Device(SpotifyObject):
  id = SpotifyID()
  is_active = graphene.Boolean()
  is_private_session = graphene.Boolean()
  is_restricted = graphene.Boolean()
  name = graphene.String()
  type = DeviceType()
  volume_percent = graphene.Int()

  @staticmethod
  def from_api(ApiData):
    fields = list(Device.__dict__.keys()) + list(Device.__dict__.keys())
    data = filter_output(ApiData, fields)
    return Device(**data)


class Query(object):
  my_devices = graphene.List(Device)

  def resolve_my_devices(self, info, **kwargs):
    if 'sp' in g:
      return [Device.from_api(d) for d in g.sp.devices()]
