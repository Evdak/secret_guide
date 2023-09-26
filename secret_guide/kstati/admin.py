from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Kstati)
class FilterKstati (admin.ModelAdmin):
    list_display = (
        "id",
        "quest_name",
        "question_number",
        "text",
        "button",
        "button_name",
        "button_on_click",
    )
    list_filter = (
        "id",
        "quest_name",
        "question_number",
        "text",
        "button",
        "button_name",
        "button_on_click",
    )
