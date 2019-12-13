import graphene
import appcompo.schema

class Query(appcompo.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
 
# class Mutation(appcompo.schema.RelayMutation,graphene.ObjectType):
#     pass
# schema = graphene.Schema(query=Query ,mutation=Mutation)
