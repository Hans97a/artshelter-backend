from django.contrib import admin
from .models import Question

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "person", "is_answered", "created_at")
    readonly_fields = ("created_at",)
