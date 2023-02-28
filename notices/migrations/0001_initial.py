# Generated by Django 4.1.7 on 2023-02-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록일자"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일자"),
                ),
                ("title", models.CharField(max_length=50, verbose_name="공지 제목")),
                (
                    "visited",
                    models.PositiveIntegerField(default=0, verbose_name="방문 횟수"),
                ),
                ("content", models.TextField(default="", verbose_name="본문")),
                ("is_pinned", models.BooleanField(default=False, verbose_name="공지사항")),
            ],
            options={
                "verbose_name_plural": "공지사항 리스트",
            },
        ),
    ]
