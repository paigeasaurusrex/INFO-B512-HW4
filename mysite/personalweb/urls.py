#myapp urls.py

from django.conf.urls import url
from . import views

urlpatterns={
			url(r'^$', views.index, name='index'),
			#url(r'^$', views.s1, name='index2'),

}


# sample url define: url(r'^others/$', views.others, name='others'),