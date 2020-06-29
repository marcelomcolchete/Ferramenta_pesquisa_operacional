from django.contrib import admin
from django.urls import path
import plataforma.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='url_home'),
]

