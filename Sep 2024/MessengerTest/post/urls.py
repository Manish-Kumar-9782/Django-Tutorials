from django.urls import path
from .views import add_post, news_feed

urlpatterns = [
    path("add",  view=add_post, name="add_post"),
    path("view",  view=news_feed, name="news_feed"),
]
