from django.conf.urls import url

# Create your tests here.

from . import views

urlpatterns = [
	url(r'^$', views.index, name ='index'),
]