from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일자")

    class Meta:
        abstract = True
