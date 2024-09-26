from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from tweets.serializer import TweetSerializer
from users.models import User
from rest_framework import status
from rest_framework.exceptions import NotFound


@api_view()
def tweets(request):
    all_tweets = Tweet.objects.all()
    seriallizer = TweetSerializer(
        all_tweets,
        many=True,
    )

    return Response(
        {
            "tweets": seriallizer.data,
        }
    )


@api_view()
def user_tweets(request, user_pk):
    try:
        user_id = User.objects.get(pk=user_pk)
    except User.DoesNotExist:
        raise NotFound(detail="User not found", code=status.HTTP_404_NOT_FOUND)
    user_tweets = Tweet.objects.filter(user=user_id)
    seriallizer = TweetSerializer(
        user_tweets,
        many=True,
    )
    return Response(
        {
            "user_tweets": seriallizer.data,
        }
    )
