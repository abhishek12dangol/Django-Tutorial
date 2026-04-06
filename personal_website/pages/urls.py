from .views import home_page_view, about_page_view
from django.urls import path

urlpatterns = [
    path("", home_page_view),
    path("about/", about_page_view),
]