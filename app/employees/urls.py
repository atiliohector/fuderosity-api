from django.conf.urls import url

from . import views

urlpatterns = (
    url('employees/', views.EmployeeViewSet.as_view(), name='employees'),
)