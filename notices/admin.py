from django.contrib import admin
from .models import Notice
from django_summernote.admin import SummernoteModelAdmin


class NoticeAdmin(SummernoteModelAdmin):
    list_display = ("title", "writer", "updated", "visited")
    readonly_fields = ("visited",)

    @admin.display(description="등록 일자")
    def updated(self, obj):
        return obj.updated_at


admin.site.register(Notice, NoticeAdmin)
