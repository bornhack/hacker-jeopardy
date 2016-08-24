from django.contrib import admin

from . import models


class AnswerInlineAdmin(admin.TabularInline):
    model = models.AnswerCategoryRelation


class CategoryInlineAdmin(admin.TabularInline):
    model = models.CategoryRoundRelation


class ContestantInline(admin.TabularInline):
    model = models.Game.contestants.through


class RoundInline(admin.TabularInline):
    model = models.RoundGameRelation


@admin.register(models.Answer)
class AnswerModelAdmin(admin.ModelAdmin):
    list_filter = ['category']


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


@admin.register(models.Round)
class RoundModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'round_type']
    inlines = [CategoryInlineAdmin]


@admin.register(models.Game)
class GameModelAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [ContestantInline, RoundInline]


@admin.register(models.Contestant)
class ContestantModelAdmin(admin.ModelAdmin):
    pass


