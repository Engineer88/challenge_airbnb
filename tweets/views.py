from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import TweetSerializer
from .models import Tweet


class AllTweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
