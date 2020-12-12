from django.urls import path
from .views import StudentAPI, GradeAPI
app_name = 'student'
# app_name = 'grade'
urlpatterns = [
    path('', StudentAPI.as_view()),
    path('<int:id>', StudentAPI.as_view()),
    path('grade/', GradeAPI.as_view()),
]