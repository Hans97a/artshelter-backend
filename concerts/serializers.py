from rest_framework import serializers
from . import models


class ConcertSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField(read_only=True)
    month = serializers.SerializerMethodField(read_only=True)
    day = serializers.SerializerMethodField(read_only=True)
    hour = serializers.SerializerMethodField(read_only=True)
    minute = serializers.SerializerMethodField(read_only=True)
    cover = serializers.SerializerMethodField()

    class Meta:
        model = models.Concert
        fields = (
            "pk",
            "title",
            "cover",
            "year",
            "month",
            "day",
            "hour",
            "minute",
            "place",
            "booking_url",
            "ticket",
            "content",
        )

    def get_year(self, obj):
        return obj.date.year

    def get_month(self, obj):
        return obj.date.month

    def get_day(self, obj):
        return obj.date.day

    def get_hour(self, obj):
        return obj.date.hour

    def get_minute(self, obj):
        return obj.date.minute

    def get_cover(self, obj):
        return self.context["request"].build_absolute_uri(obj.cover.url)
