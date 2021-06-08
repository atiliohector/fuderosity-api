from django.urls import path

from . import views

urlpatterns = [
    path("",views.AllEmployees.as_view(),name="todo_list"),
    path("create/", views.CreateEmployee.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateEmployee.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteEmployee.as_view(),name="delete_todo")
]