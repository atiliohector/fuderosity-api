from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.EmployeesViews.as_view(), name='employees'),
)