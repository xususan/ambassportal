from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ambassportal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.populate_home_page),
    #url(r'^profile/', views.populate_profile),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?P<url>.*/)$', views.flatpage),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
