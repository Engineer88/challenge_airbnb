from django.urls import path
from . import views

urlpatterns = [
    path("tweets/", views.tweets),
    path("users/<int:user_pk>/tweets/", views.user_tweets),
]
