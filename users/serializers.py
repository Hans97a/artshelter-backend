from rest_framework import serializers
from users import models


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("nickname",)
