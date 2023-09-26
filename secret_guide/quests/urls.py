from django.urls import path
from . import views


urlpatterns = [
    path('',
         views.quest_list, name='quest_list'),
    path('instruction',
         views.instruction, name='instruction'),
    path('card',
         views.card, name='card'),
    path('<str:quest_name>',
         views.index, name='index'),
    path('<str:folder>/<str:filename>',
         views.static, name='static')
]
