"""NIP_checker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from NIP_checker_app.views import NIPView, \
    Login4View, LogoutView, NipListView, NipListCheckView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^create_nip', NIPView.as_view(), name='create_nip'),
    url(r'^userlogin', Login4View.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name = 'logout'),
    url(r'^nip_list', NipListView.as_view(), name='nip_list'),
    url(r'^check_nip_list', NipListCheckView.as_view(), name='check_nip_list'),
]

urlpatterns += [
    url(r'^django-rq/', include('django_rq.urls')),
]