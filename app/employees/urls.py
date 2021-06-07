from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.fuderosity_employees, name='employees'),
)