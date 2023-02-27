from rest_framework import serializers
from . import models
from users.serializers import TinyUserSerializer


class NoticeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d")
    writer = TinyUserSerializer(read_only=True)

    class Meta:
        model = models.Notice
        fields = (
            "pk",
            "title",
            "writer",
            "is_pinned",
            "content",
            "visited",
            "created_at",
            "updated_at",
        )
