from rest_framework import serializers
from .models import *


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):


    class Meta:
        model = Commentaire
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    articlecommentaire = CommentaireSerializer(many=True, read_only=True, required=False)
    articletag = TagSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'

class AuteurSerializer(serializers.ModelSerializer):
    auteurarticle = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Auteur
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    categoriearticle = ArticleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Categorie
        fields = '__all__'
