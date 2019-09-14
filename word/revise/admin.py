# from django.contrib import admin

# # Register your models here.
# # vim: set fileencoding=utf-8 :
# from django.contrib import admin

# from . import models


# class PostAdmin(admin.ModelAdmin):

#     list_display = (
#         'id',
#         'image',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#         'Categorie_id',
#     )
#     list_filter = (
#         'date_add',
#         'date_upd',
#         'statut',
#         'Categorie_id',
#         'id',
#         'image',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#         'Categorie_id',
#     )


# class CategorieAdmin(admin.ModelAdmin):

#     list_display = (
#         'id',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#     )
#     list_filter = (
#         'date_add',
#         'date_upd',
#         'statut',
#         'id',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#     )


# class CommentaireAdmin(admin.ModelAdmin):

#     list_display = (
#         'id',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#         'Post_id',
#     )
#     list_filter = (
#         'date_add',
#         'date_upd',
#         'statut',
#         'Post_id',
#         'id',
#         'titre',
#         'description',
#         'date_add',
#         'date_upd',
#         'statut',
#         'Post_id',
#     )


# def _register(model, admin_class):
#     admin.site.register(model, admin_class)


# _register(models.Post, PostAdmin)
# _register(models.Categorie, CategorieAdmin)
# _register(models.Commentaire, CommentaireAdmin)
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
# Configuration du site

admin.site.site_title = "Mon super site"
admin.site.site_header = "NaN"


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'Categorie_id',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'Categorie_id',
        'id',
        'image',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'Categorie_id',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'affiche_image',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
    )

    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))



class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'Post_id',
    )
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'Post_id',
        'id',
        'titre',
        'description',
        'date_add',
        'date_upd',
        'statut',
        'Post_id',
    )


class UtiliAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_upd')
    list_filter = (
        'date_add',
        'date_upd',
        'id',
        'nom',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Post, PostAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Utili, UtiliAdmin)


