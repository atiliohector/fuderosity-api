from django.urls import path, include

from . import views


urlpatterns = [
    path('all/', views.AllStudent.as_view()),
    path('create/', views.AddStudent.as_view()),
    path('<int:id>/', views.SpecifStudent.as_view()),
]