"""dubhacksProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.db import connection
from dubhacksProj.views import women, hcde, cse, info, about, engineer

cursor = connection.cursor()
cursor.execute('SELECT Name, Major, Response1, Response2, Response3, Response4, Response5, Image FROM dubhacksapp_personentry')
row = cursor.fetchall()
list = []
for x in row:
    list.append(x[0])

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', women, name='women'),
    url(r'^women/$', women),
    url(r'^hcde/$', hcde, name='hcde'),
    url(r'^info/$', info, name='info'),
    url(r'^cse/$', cse, name='cse'),
    url(r'^about/$', about, name='about'),
    url(r'^women/(\d{0,len(list)-1})$', engineer, name='engineer')
]
