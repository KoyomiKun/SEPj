from django.contrib import admin
from django.urls import include, path
from .views import get_record, get_user, search

urlpatterns = [
    path('records/', get_record),
    path('user/<int:id>', get_user),
    path('search/<int:id>', search)
]
