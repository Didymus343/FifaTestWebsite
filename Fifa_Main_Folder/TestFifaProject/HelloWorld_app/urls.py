from django.conf.urls import url
from HelloWorld_app import views


urlpatterns = [

    #url(r'^$', views.index, name='welcome'),
    url(r'^$', views.help, name='help'),

]
