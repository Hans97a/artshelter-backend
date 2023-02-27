from rest_framework import serializers
from . import models
from users.serializers import TinyUserSerializer


class EducationSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d")
    year = serializers.SerializerMethodField(read_only=True)
    cover = serializers.SerializerMethodField()

    class Meta:
        model = models.Education
        fields = ("pk", "title", "cover", "blog_url", "created_at", "year")

    def get_year(self, obj):
        return obj.created_at.year

    def get_cover(self, obj):
        return self.context["request"].build_absolute_uri(obj.cover.url)
