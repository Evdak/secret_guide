from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(IconsWhy)
class FilterIconsWhy(admin.ModelAdmin):
    list_display = (
        "id",
        "header",
        "description",
    )

    list_filter = (
        "id",
        "header",
        "description",
    )


@admin.register(IconsWhen)
class FilterIconsWhen(admin.ModelAdmin):
    list_display = (
        "id",
        "header",
        "description",
    )

    list_filter = (
        "id",
        "header",
        "description",
    )


@admin.register(Photo)
class FilterPhoto(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "file",
    )
    list_filter = (
        "id",
        "name",
        "file",
    )


@admin.register(Video)
class FilterVideo(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "file",
    )
    list_filter = (
        "id",
        "name",
        "file",
    )


@admin.register(Review)
class FilterReview(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "text",
        "photo",
    )
    list_filter = (
        "id",
        "name",
        "text",
        "photo",
    )


@admin.register(Quest)
class FilterQuest(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
        "what_waits_you",
        "get_why_it_need",
        "get_when_it_need",
        "get_photo",
        "get_video",
        "get_reviews",
    )
    list_filter = (
        "id",
        "name",
        "description",
        "price",
    )
