from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_student/', views.add_student, name='add_student'),
    path('save_image/', views.save_image, name='save_image'),
    path('recognize_student/', views.recognize_student, name='recognize_student'),
    path('recognize_face/', views.recognize_face, name='recognize_face'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
]