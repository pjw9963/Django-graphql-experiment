import graphene
import cookbook.ingredients.schema

class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    #this class will inherit more queries as we add more apps
    pass

schema = graphene.Schema(query=Query)