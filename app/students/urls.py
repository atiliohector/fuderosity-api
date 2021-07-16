from django.urls import path, include

from . import views


urlpatterns = [
    path('all/', views.AllStudent.as_views())
]