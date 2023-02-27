from django.db import models
from common.models import TimeStampedModel
from common.utils import upload_to

# Create your models here.


class Concert(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="공연 제목")
    writer = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name="작성자"
    )
    cover = models.ImageField(
        blank=False, upload_to=upload_to("concerts", True), verbose_name="공연 대표 이미지"
    )
    is_banner = models.BooleanField(default=False, verbose_name="메인 페이지 배너 사용 유무")
    date = models.DateTimeField(verbose_name="공연 일자")
    place = models.CharField(max_length=50, verbose_name="공연 장소")
    booking_url = models.CharField(max_length=250, verbose_name="예매 링크")
    ticket = models.CharField(max_length=50, verbose_name="티켓 가격 정보")
    content = models.TextField(default="", verbose_name="본문")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "공연 리스트"
