# Generated by Django 4.1.7 on 2023-02-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("concerts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="concert",
            name="booking_url",
            field=models.CharField(default="fff", max_length=250, verbose_name="예매 링크"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="concert",
            name="context",
            field=models.TextField(default="", verbose_name="본문"),
        ),
    ]
