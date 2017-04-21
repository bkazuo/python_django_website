from django.conf.urls import url
from . import views # Import from the very app


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
]