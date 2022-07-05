from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render


from .models import *
# Create your views here.


def index(request: HttpRequest, quest_name: str):
    quest = Quest.objects.filter(
        name=quest_name).first()
    print(quest.photo.all())
    if quest:
        return render(request, 'quest.html', {'quest': quest})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def test(request: HttpRequest):
    return HttpResponse('<h1>123</h1>')


def static(request: HttpRequest, folder: str, filename: str):
    print('da')
    try:
        with open(f'static/{folder}/{filename}', "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        # red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        # response = HttpResponse(content_type="image/jpeg")
        # red.save(response, "JPEG")
        # return response
        return None
