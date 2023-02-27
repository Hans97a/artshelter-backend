from django.contrib import admin
from .models import Concert
from django_summernote.admin import SummernoteModelAdmin


class ConcertAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)
    list_display = ("title", "writer", "updated")

    @admin.display(description="등록 일자")
    def updated(self, obj):
        return obj.updated_at


admin.site.register(Concert, ConcertAdmin)
