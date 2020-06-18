from django.urls import path
from .views import *
urlpatterns = [
    path('shifts',ShiftView.as_view()),
    path('people',PersonView.as_view()),
    path('export/<str:shift_id>',export)
]
