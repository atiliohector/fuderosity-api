from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.beautiful_employees, name='employees'),
)