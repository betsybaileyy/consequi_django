from django.shortcuts import render
from django.http import HttpResponse
from goal.models import Achievement, Goal


def index(request):
    all_achievements = Achievement.objects.filter(name="Hello World")
    all_goals = Goal.objects.all()
    return HttpResponse(f"# of Achievements: <br># of Goals: {all_achievements}<br> # of goals: {len(all_goals)} ")
