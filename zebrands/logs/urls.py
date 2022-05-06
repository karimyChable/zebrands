from django.urls import path

from zebrands.logs.views import LogView, LogListView

logs_urls = [
    path("logs/<uuid:pk>", LogView.as_view()),
    path("logs/", LogListView.as_view()),
]
