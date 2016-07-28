from django.contrib import admin

from . import models


@admin.register(models.Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    pass


class AnswerInlineAdmin(admin.TabularInline):
    model = models.Answer


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


@admin.register(models.Round)
class RoundModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Game)
class GameModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Player)
class PlayerModelAdmin(admin.ModelAdmin):
    pass

