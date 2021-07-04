from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllManagers.as_view()),
    path('create/', views.AddManager.as_view()),
    path('manager/<int:id>/', views.ManagerById.as_view()),
    path('champions/', views.ManagersChampions.as_view())

]