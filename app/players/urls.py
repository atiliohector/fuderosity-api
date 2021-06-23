from django.urls import path, include

from . import views

urlpatterns = [

    path('create/', views.CreatePlayers.as_view(), name='create_players'),
    path('', views.AllPlayers.as_view(),name='all_players'),
    path('delete/<int:id>/',views.DeletePlayers.as_view(),name='delete_players'),
    path('update/<int:id>/',views.UpdatePlayers.as_view(),name='update_players'),

]