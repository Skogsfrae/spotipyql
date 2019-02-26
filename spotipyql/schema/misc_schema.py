import graphene


class Image(graphene.ObjectType):
  url = graphene.String()
  height = graphene.Int()
  width = graphene.Int()
