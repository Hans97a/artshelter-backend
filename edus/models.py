from django.db import models
from common.utils import upload_to
from common.models import TimeStampedModel

# Create your models here.


class Education(TimeStampedModel):
    title = models.CharField(max_length=100, verbose_name="블로그 제목")
    cover = models.ImageField(
        blank=False, upload_to=upload_to("edus", True), verbose_name="대표 이미지"
    )
    blog_url = models.CharField(max_length=250, verbose_name="블로그 링크")
    # content = models.TextField(default="", verbose_name="본문")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "교육 정보 리스트"
