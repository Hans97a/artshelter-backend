# Generated by Django 4.1.7 on 2023-03-02 09:47

import common.utils
from django.db import migrations, models
import functools


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
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
                ("title", models.CharField(max_length=100, verbose_name="블로그 제목")),
                (
                    "cover",
                    models.ImageField(
                        upload_to=functools.partial(
                            common.utils._update_filename,
                            *(),
                            **{"hash": True, "path": "edus"}
                        ),
                        verbose_name="대표 이미지",
                    ),
                ),
                ("blog_url", models.CharField(max_length=250, verbose_name="블로그 링크")),
            ],
            options={
                "verbose_name_plural": "교육 정보 리스트",
            },
        ),
    ]
