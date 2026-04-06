from django.urls import path
from .views import PostList

urlpatterns = [
    path("message/",PostList.as_view(), name="message" ),
]