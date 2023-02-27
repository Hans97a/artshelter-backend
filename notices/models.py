from django.db import models
from common.models import TimeStampedModel


class Notice(TimeStampedModel):
    title = models.CharField(max_length=50, verbose_name="공지 제목")
    writer = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name="작성자"
    )
    visited = models.PositiveIntegerField(default=0, verbose_name="방문 횟수")
    content = models.TextField(default="", verbose_name="본문")
    is_pinned = models.BooleanField(default=False, verbose_name="공지사항")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "공지사항 리스트"
