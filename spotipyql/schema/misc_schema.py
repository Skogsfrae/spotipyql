import graphene


class Image(graphene.ObjectType):
  url = graphene.String()
  height = graphene.Int()
  width = graphene.Int()


class TimeInterval(graphene.ObjectType):
  start = graphene.Float()
  duration = graphene.Float()
  confidence = graphene.Float()


class Section(graphene.ObjectType):
  start = graphene.Float()
  duration = graphene.Float()
  confidence = graphene.Float()
  loudness = graphene.Float()
  tempo = graphene.Float()
  tempo_confidence = graphene.Float()
  key = graphene.Int()
  key_confidence = graphene.Float()
  mode = graphene.Int()
  mode_confidence = graphene.Float()
  time_signature = graphene.Int()
  time_signature_confidence = graphene.Float()


class Segment(graphene.ObjectType):
  start = graphene.Float()
  duration = graphene.Float()
  confidence = graphene.Float()
  loudness_start = graphene.Float()
  loudness_max_time = graphene.Float()
  loudness_max = graphene.Float()
  loudness_end = graphene.Float()
  pitches = graphene.List(graphene.Float)
  timbre = graphene.List(graphene.Float)