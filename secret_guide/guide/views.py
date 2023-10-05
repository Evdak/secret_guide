from django.shortcuts import render
from django.http import HttpRequest

from guide.models import *

import logging


def index(request: HttpRequest):
    categories = (
        Category
        .objects
        .order_by("position")
        .all()
    )
    _data = []
    for cat in categories:
        places = (
            Place
            .objects
            .filter(category=cat)
            .order_by("position")
            .all()
        )
        if places:
            _data.append(
                {
                    "category": cat,
                    "places": places,
                }
            )

    logging.warning(categories)

    return render(
        request,
        "guide_index.html",
        {
            "data": _data,
        }
    )
