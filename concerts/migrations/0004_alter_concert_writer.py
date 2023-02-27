# Generated by Django 4.1.7 on 2023-02-17 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("concerts", "0003_rename_context_concert_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="concert",
            name="writer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="작성자",
            ),
        ),
    ]
