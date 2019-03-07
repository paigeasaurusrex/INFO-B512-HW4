from django.conf.urls import url
from . import views

urlpatterns=[
			url(r'^$', views.index, name='index'),
			url(r'^delete_project/(?P<project_id>[0-9]+)$', views.delete_project, name='deleteproject'),
			url(r'^delete_skill/(?P<skill_id>[0-9]+)$', views.delete_skill, name='deleteskill'),
			url(r'^insert_project/$', views.insert_project, name='insertproject'),

]
