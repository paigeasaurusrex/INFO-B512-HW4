
'''django2 version'''
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('personalweb/', include('personalweb.urls')),
    path('admin/', admin.site.urls),
]

'''django1 version'''
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
	url(r'^personalweb/', include('personalweb.urls')),
    url(r'^admin/', admin.site.urls),    
]



