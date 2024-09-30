from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/tweets", views.UserTweets.as_view()),
    path("", views.UserList.as_view()),
    path("<int:pk>", views.UserDetail.as_view()),
]
