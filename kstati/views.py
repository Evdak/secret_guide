from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render


from .models import *
# Create your views here.


def index(request: HttpRequest, quest_name: str, question_number: int):
    kstati = Kstati.objects.filter(
        quest_name=quest_name, question_number=question_number).first()
    if kstati:
        return render(request, 'index.html', {'kstati': kstati})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def test(request: HttpRequest):
    return HttpResponse('<h1>123</h1>')
