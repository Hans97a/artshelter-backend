from django.db import models
from common.models import TimeStampedModel

# Create your models here.


MESSAGE_TYPE_CHOICES = (("concert", "공연 문의"), ("edu", ("교육 문의")), ("etc", "기타"))


class Question(TimeStampedModel):
    title = models.CharField(max_length=120, verbose_name="문의 제목")
    person = models.CharField(max_length=254, verbose_name="성함 혹은 기관 이름")
    contact = models.CharField(max_length=254, verbose_name="문의자 연락처")
    type = models.CharField(
        max_length=20, choices=MESSAGE_TYPE_CHOICES, verbose_name="문의 종류"
    )
    content = models.TextField(default="", verbose_name="문의 내용")
    is_answered = models.BooleanField(default=False, verbose_name="답변 여부")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "문의 리스트"
