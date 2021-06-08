from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.employee_totaly, name='employees'),
)