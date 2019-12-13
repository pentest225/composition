import graphene
from graphene import relay, ObjectType , Connection , Node,Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models
from django_filters import OrderingFilter 
from graphql_relay import from_global_id

class ExtendConnection(Connection):
    class Meta:
        abstract = True

    total_count = Int()
    edge_count = Int()

    def resolve_total_count(root, info, **kwargs):
        return root.length
    def resolve_edge_count(root, info, **kwargs):
        return len(root.edges)



class CategorieNode(DjangoObjectType):
   class Meta:
        model = models.Categorie
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class AuteurNode(DjangoObjectType):
       class Meta:
        model = models.Auteur
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class ArticleNode(DjangoObjectType):
       class Meta:
        model = models.Article
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'auteur': ['exact',],
            'titre': ['exact', 'icontains', 'istartswith'],
            'titre_slug': ['exact'],
            'description': ['exact', 'icontains', 'istartswith'],
            'categorie': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class CommentaireNode(DjangoObjectType):
       class Meta:
        model = models.Commentaire
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'email': ['exact',],
            'message': ['exact', 'icontains', 'istartswith'],
            'article': ['exact'],
            'Website': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection

class TagNode(DjangoObjectType):
       class Meta:
        model = models.Tag
        # Allow for some more advanced filtering here
        fields = "__all__"
        filter_fields = {
            'nom': ['exact', 'icontains', 'istartswith'],
            'article': ['exact'],
            'status': ['exact'],
        }
        interfaces = (relay.Node, )
        connection_class = ExtendConnection
        
# #Auteur mutation
# class RelayCreateAuthor(graphene.relay.ClientIDMutation):
#     author = graphene.Field(AuthorNode)
#     class Input:
#         name = graphene.String()
#         status = graphene.Boolean()
#     def mutate_and_get_payload(root,info,**kwargs):
#         name = kwargs.get('nom') or None
#         #default status False
#         status = False
#         if name is not None and not name.isspace():
#             author = models.Author(name=name, status=status)
#         else:
#             raise Exception('les paramettre sont requis')
#         author.save()
#         return RelayCreateAuthor(author=author)
    
        
   
# class BookNode(DjangoObjectType):
#    class Meta:
#         model = models.Book
#         # Allow for some more advanced filtering here
#         fields = "__all__"
#         filter_fields = {
#             'title': ['exact', 'icontains', 'istartswith'],
#             'author': ['exact'],
#             'statut': ['exact'],
#         }
#         interfaces = (relay.Node, )
#         connection_class = ExtendConnection
# # book mutation
# class RelayCreateBook(graphene.relay.ClientIDMutation):
#     book = graphene.Field(BookNode)
#     class Input:
#         author = graphene.ID()
#         title = graphene.String()
#         description = graphene.String()
#         status = graphene.Boolean()
        
#     def mutate_and_get_payload(root,info,**kwargs):

#         author = kwargs.get('quest') or None
#         title = kwargs.get('code_test') or None
#         description = kwargs.get('resultat') or None
        
#         book = None
#         if author:
#             author = from_global_id(author)
#             author=author[1]
#             author = models.Author.objects.get(id=author)
#         data = {
#             'author':author,
#             'title':title,
#             'description':description,
#             #default status False
#             'status': Fasle,
#         }
#         if title and author and description and status :
                
#             book = models.Book(
#             **data
#             )

#             book.save()
                
#             return RelayCreateBook(book=book)
#         else:
            
#             raise Exception('les paramettre sont requis')


class Query(graphene.ObjectType):
    categorie = relay.Node.Field(CategorieNode)
    all_categorie = DjangoFilterConnectionField(CategorieNode)
    
    auteur = relay.Node.Field(AuteurNode)
    all_auteur = DjangoFilterConnectionField(AuteurNode)

    article = relay.Node.Field(ArticleNode)
    all_article = DjangoFilterConnectionField(ArticleNode)

    commentaire = relay.Node.Field(CommentaireNode)
    all_commentaire = DjangoFilterConnectionField(CommentaireNode)

    tag = relay.Node.Field(TagNode)
    all_tag = DjangoFilterConnectionField(TagNode)

# class RelayMutation(graphene.AbstractType):
#     relay_create_author = RelayCreateAuthor.Field()
#     relay_create_book = RelayCreateBook.Field()
