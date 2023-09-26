from django.http import HttpRequest, HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .functions import paste_watermark_on_image
from secret_guide.settings import ALLOWED_HOSTS

import json


def index(request: HttpRequest, quest_name: str):
    quest = Quest.objects.filter(
        name=quest_name).first()
    logging.warning(quest.photo.all())
    if quest:
        return render(request, 'quest.html', {'quest': quest})
    else:
        return HttpResponseNotFound('<h1>Страница не найдена</h1>')


@csrf_exempt
def card(request: HttpRequest):
    body = json.loads(request.body)
    image_url = body.get('url')
    print(f"{image_url=}")
    quest_type = body.get('quest_type')
    card_url = paste_watermark_on_image(image_url, quest_type)
    if card_url:
        return JsonResponse({"result": f"http://{ALLOWED_HOSTS[-1]}/media/{card_url}"})
    else:
        return JsonResponse({"result": f"Произошла ошибка"})


def quest_list(request: HttpRequest):
    quest = Quest.objects.all()
    return render(request, 'quests_list.html', {'quest': quest})


def instruction(request: HttpRequest):
    return render(request, "instruction.html")


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
