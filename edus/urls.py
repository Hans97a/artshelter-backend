from django.urls import path
from . import views


urlpatterns = [
    path("", views.EducationListView.as_view()),
    path("<int:pk>", views.EducationDetailView.as_view()),
]
