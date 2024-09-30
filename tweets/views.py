from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from .serializer import TweetSerializer
from .models import Tweet


class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            tweets = serializer.save()
            serializer = TweetSerializer(tweets)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TweetsDetail(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetSerializer(tweet)
        return Response(serializer.data)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        serializer = TweetSerializer(
            self.get_object(pk),
            data=request.data,
            partiarl=True,
        )
        if serializer.is_valid():
            updated_tweet = serializer.save()
            serializer = TweetSerializer(updated_tweet)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
