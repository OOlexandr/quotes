from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<str:author_name>', views.author, name='author'),
]