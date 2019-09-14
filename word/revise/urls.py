from . import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('contact',views.contact),
    path('regular',views.regular),
    path('blog',views.blog),
    path('categorie',views.categorie),
]