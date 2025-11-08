from django.contrib import admin

from .models import Bot, Scenario, Step


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ['name', 'token', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['title', 'bot', 'created_at']
    list_filter = ['bot', 'created_at']
    search_fields = ['title']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['order', 'scenario', 'prompt']
    list_filter = ['scenario']
    search_fields = ['prompt']
