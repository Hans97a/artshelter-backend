from django.urls import path
from . import views


urlpatterns = [
    path("", views.ConcertListView.as_view()),
    path("<int:pk>", views.ConcertDetailView.as_view()),
    path("banner", views.ConcertBannerView.as_view()),
]
