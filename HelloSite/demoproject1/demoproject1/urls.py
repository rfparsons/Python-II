"""demoproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from helloworld import views as hello_view
from to_do import views as to_do_view
from graph import views as graph_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url('to_do/', to_do_view.to_do, name='to do list'),
    url('graph/', graph_view.graph, name='my graph'),
    url('graph2/', graph_view.graph2, name='my graph'),
    url(r'^$', hello_view.home, name='home'),
]
