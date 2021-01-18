from django.urls import path, re_path, register_converter
from . import views
# , converters



urlpatterns = [
    path('index', views.books_short),
]