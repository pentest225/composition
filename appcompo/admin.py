from django.contrib import admin

from . import models
# from django.contrib.postgres import fields
# from django_json_widgets import JSonEditorWiqget
# from django.utils.safestring import mark_safe
 


class CategorieAdmin(admin.ModelAdmin):

    list_display = ('nom','titre_slug', 'status', 'date_add', 'date_upd')
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'nom',
        'titre_slug',
    )
    


class AuteurAdmin(admin.ModelAdmin):

    list_display = (
        'image',
        'nom',
        'titre_slug',
        
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'nom',
        
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'categorie',
        'auteur',
        'titre',
        'titre_slug',
        'image',
    )
    list_filter = (
        'categorie',
        'status',
        'date_add',
        'date_upd',
        'auteur',
        'titre',
        'image',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'article',
        'nom',
        'email',
        'Website',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'article',
        'status',
        'date_add',
        'date_upd',
        'article',
        'nom',
        'email',
        'Website',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('article', 'nom', 'status', 'date_add', 'date_upd')
    list_filter = (
        'article',
        'status',
        'date_add',
        'date_upd',
        'article',
        'nom',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Auteur, AuteurAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Tag, TagAdmin)
