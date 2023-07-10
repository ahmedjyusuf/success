from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user

User = get_user

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email','first_name', 'last_name', 'password')