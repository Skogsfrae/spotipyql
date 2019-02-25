from datetime import datetime, date

import graphene
from graphene import Node, relay, Connection

from flask import g

from spotipyql.utils import filter_output
from spotipyql.schema.user_schema import PublicUser
from spotipyql.schema.media_schema import Track


class PlaylistTrack(graphene.ObjectType):
  added_at = graphene.DateTime()
  added_by = graphene.Field(lambda: PublicUser)
  is_local = graphene.Boolean()
  # primary_color = graphene.?????
  track = graphene.Field(lambda: Track)


class Playlist(graphene.ObjectType):
  id = graphene.String()
  name = graphene.String()
  collaborative = graphene.Boolean()
  # TODO: images = graphene.String()
  owner = graphene.Field(lambda: PublicUser)
  public = graphene.Boolean()
  snapsho_id = graphene.String()
  tracks = graphene.List(lambda: PlaylistTrack)
  type = graphene.String()
  uri = graphene.String()

  @staticmethod
  def from_api(ApiData):
    data = filter_output(ApiData, Playlist.__dict__.keys())
    return Playlist(**data)



class Query(object):
  playlist = graphene.Field(Playlist)