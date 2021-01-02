from django.urls import path
from .views import SeqApi, CompApi, GenApi, ParApi

app_name = 'special_fields'

urlpatterns = [
    path('seq/', SeqApi.as_view()),
    path('comp/', CompApi.as_view()),
    path('gen/', GenApi.as_view()),
    path('par/', ParApi.as_view()),
]