from datetime import datetime, date

import graphene
from graphene import Node, relay, Connection

from flask import g

from spotipyql.utils import filter_output


class User(graphene.Interface):
  id = graphene.String()
  display_name = graphene.String()
  # TODO: external_urls
  # TODO: followers
  # TODO: images
  type = graphene.String()
  uri = graphene.String()


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
    return PrivateUser(**data)


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
      return PublicUser.from_api(g.sp.public_user(id))