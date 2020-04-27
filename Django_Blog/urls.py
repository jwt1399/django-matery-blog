"""Django_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from blog import views
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    # #首页
    # path('', views.index,name='index'),
    # #文章详情页
    # path('',views.article_detail,name='article_detail')
    #path('favicon.ico', serve, {'path': 'static/img/favicon.ico'}),
    #path('favicon.ico', RedirectView.as_view(url='static/img/favicon.ico')),
    path('',include('blog.urls')),
    path('mdeditor/',include('mdeditor.urls')),
]
