"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myproject.authtentifikasi import akun_login, akun_registrasi
from myproject.views import (
    home,
    upload_berkas,
    contact,
    dashboard,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('form-pendaftaran/', form_pendaftaran, name='form-pendaftaran'),
    path('upload-berkas/', upload_berkas, name='upload-berkas'),
    path('contact/', contact, name='contact'),
    path('authentifikasi/login', akun_login, name='akun_login'),
    # path('logout/', akun_logout, name='logout'),
    path('authentifikasi/registrasi', akun_registrasi, name='akun_registrasi'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', include('pengguna.urls')),
    # path('create_formulir',create_formulir,name='formulir'),
]

