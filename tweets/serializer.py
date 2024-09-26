from rest_framework import serializers
from users.models import User


class TweetSerializer(serializers.Serializer):

    pk = serializers.IntegerField()
    payload = serializers.CharField(
        required=True,
    )
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    created_at = serializers.DateTimeField()
