from django.urls import path

from . import views

urlpatterns = [
    
    path('create/', views.CreateManager.as_view(),name='create_managers'),
    path('', views.AllManagers.as_view(),name='all_managers'),
    path('delete/<int:id>/', views.DeleteManagers.as_view(),name='delete_manager'),
    path('update/<int:id>/',views.UpdateManagers.as_view(), name='update_manager'),
]