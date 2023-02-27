from django.contrib import admin
from .models import Question

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "person", "created_at")
    readonly_fields = ("created_at",)
