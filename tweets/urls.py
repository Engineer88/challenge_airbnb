from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllTweets.as_view()),
]
