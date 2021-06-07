from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.employees_all, name='employees'),
)