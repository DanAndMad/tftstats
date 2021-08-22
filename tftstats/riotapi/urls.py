from django.urls import path
from .views import *

urlpatterns = [
    path('get-league', LeagueList.as_view()),
    path('get-matches', Matches.as_view())
]