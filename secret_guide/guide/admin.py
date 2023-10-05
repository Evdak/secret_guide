from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class FilterCategory(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "position",
    )
    list_filter = list_display


@admin.register(Place)
class FilterPlace(admin.ModelAdmin):
    list_display = (
        "category",
        "title",
        "address",
        "map_url",
        "photo",
        "position",
    )
    list_filter = list_display
