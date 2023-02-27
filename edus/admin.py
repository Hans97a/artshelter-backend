from django.contrib import admin
from .models import Education
from django_summernote.admin import SummernoteModelAdmin


class EducationAdmin(SummernoteModelAdmin):
    list_display = ("title", "updated")
    search_fields = ("title",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    @admin.display(description="등록 일자")
    def updated(self, obj):
        return obj.updated_at


admin.site.register(Education, EducationAdmin)
