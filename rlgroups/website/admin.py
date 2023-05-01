from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Team, Feedback

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, obj) -> bool:
        return False
