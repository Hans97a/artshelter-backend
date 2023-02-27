from rest_framework import serializers
from . import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ("title", "contact", "type", "content", "person")
