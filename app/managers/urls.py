from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.TodoListApiView.as_view()),

]