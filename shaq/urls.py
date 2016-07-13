"""shaq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth import urls as auth_urls
from django.shortcuts import render

urlpatterns = [
    url(r'^$', lambda request: render(request, 'landing_page/landing_page.html')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^home$', lambda request: render(request, 'shaq/shaq_home.html'), name='site_home'),
    url(r'^admin/', admin.site.urls),
]
