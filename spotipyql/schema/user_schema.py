import graphene

from flask import g

from spotipyql.utils import filter_output

import spotipyql.schema.playlist_schema as playlist_schema
import spotipyql.schema.misc_schema as misc_schema


class User(graphene.Interface):
  id = graphene.String()
  display_name = graphene.String()
  # TODO: external_urls
  # TODO: followers
  images = graphene.List(lambda: misc_schema.Image)
  type = graphene.String()
  uri = graphene.String()
  playlists = graphene.List(lambda: playlist_schema.Playlist, first=graphene.Int(), offset=graphene.Int())

  def resolve_playlists(self, info, first=10, offset=0):
    if 'sp' in g:
      data = g.sp.user_playlists(self.id, first, offset)
      return [playlist_schema.Playlist.from_api(p, self) for p in data['items']]


class PrivateUser(graphene.ObjectType):
  class Meta:
    interfaces = (User,)

  email = graphene.String()
  country = graphene.String()
  product = graphene.String()
  uri = graphene.String()

  @staticmethod
  def from_api(ApiData):
    fields = list(PrivateUser.__dict__.keys()) + list(User.__dict__.keys())
    data = filter_output(ApiData, fields)
    user = PrivateUser(**data)
    user.images = [misc_schema.Image(**img) for img in data['images']]
    return user


class PublicUser(graphene.ObjectType):
  class Meta:
    interfaces = (User,)

  @staticmethod
  def from_api(ApiData):
    fields = list(PublicUser.__dict__.keys()) + list(User.__dict__.keys())
    data = filter_output(ApiData, fields)
    return PublicUser(**data)


class Query(object):
  me = graphene.Field(PrivateUser)
  public_user = graphene.Field(PublicUser, id=graphene.String())

  def resolve_me(self, info, **kwargs):
    if 'sp' in g:
      return PrivateUser.from_api(g.sp.me())

  def resolve_public_user(self, info, id, **kwargs):
    if 'sp' in g:
      return PublicUser.from_api(g.sp.user(id))