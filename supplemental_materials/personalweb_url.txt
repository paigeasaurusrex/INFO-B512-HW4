from django.conf.urls import url
from . import views

urlpatterns={
			url(r'^$', views.index, name='index'),

}


# sample url define: url(r'^others/$', views.others, name='others'),