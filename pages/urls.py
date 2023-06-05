from django.urls import path
from .views import HomePageView, AboutPageView


urlpatterns = [
    path("", HomePageView.AS_VIEW(), name="home"),
    path("", AboutPageView.AS_VIEW(), name="about"),
]