from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^employees/$', views.EmployeeViewSet.as_view(), name='employees'),
)