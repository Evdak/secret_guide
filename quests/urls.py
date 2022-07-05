from django.urls import path
from . import views


urlpatterns = [
    path('<str:quest_name>',
         views.index, name='index'),
    path('<str:folder>/<str:filename>',
         views.static, name='static')
]
