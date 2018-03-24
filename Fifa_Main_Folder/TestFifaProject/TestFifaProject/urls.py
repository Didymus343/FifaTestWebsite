"""TestFifaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# provides ability to add complete url.py from application level to project views
from django.conf.urls import include
# Example of a single reference to a application view
from HelloWorld_app import views


urlpatterns = [
    url(r'^help/', include('HelloWorld_app.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
