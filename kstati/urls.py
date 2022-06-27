from django.urls import path
from . import views


urlpatterns = [
    path('<str:quest_name>/<int:question_number>',
         views.index, name='index'),
    path('', views.test, name='test')
]
