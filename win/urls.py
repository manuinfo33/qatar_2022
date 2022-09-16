from django.contrib import admin
from django.urls import path
from win.views import create_participant,list_participants

urlpatterns = [
    path('new-participant/', create_participant, name='create_participant'),
    path('all-participants/', list_participants, name='list_participants'),
    ]