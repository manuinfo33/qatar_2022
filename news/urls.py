from django.contrib import admin
from django.urls import path
from news.views import create_article, list_articles, delete_article, update_articles


urlpatterns = [
    path('new-article/', create_article, name='create_article'),
    path('all-articles/', list_articles, name='list_articles'),
    path('delete-articles/<int:pk>/', delete_article, name='delete_articles'),
    path('update-articles/<int:pk>/', update_articles, name='update_articles'),
]