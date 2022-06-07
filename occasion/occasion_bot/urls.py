from django.urls import path
from occasion_bot.views import index


urlpatterns = [
    path('', index),
]