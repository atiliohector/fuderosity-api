from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'employes', include('app.employees.urls')),
    path(r'companies', include('app.companies.urls'))
]
