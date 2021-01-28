from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'<book_id>/', views.detail, name='detail')
]