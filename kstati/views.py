from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render


from .models import *
# Create your views here.


def index(request: HttpRequest, quest_name: str, question_number: int):
    kstati = Kstati.objects.filter(quest_name=quest_name).first()
    if kstati:
        return render(request, 'index.html', {'kstati': kstati})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')
