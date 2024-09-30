from rest_framework.serializers import ModelSerializer
from .models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
        ]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
        ]
