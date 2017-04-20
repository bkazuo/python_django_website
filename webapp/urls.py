from django.conf.urls import url
from . import views # Import from the very app


urlpatterns = [
url(r'^hey$', views.index, name='index')]