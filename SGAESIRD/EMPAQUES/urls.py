from django.urls import path
from . import views
import functools

from django.conf.urls import url
from django.conf import settings
from django.urls import LocalePrefixPattern, URLResolver, get_resolver, path
from django.views.i18n import set_language


urlpatterns = [
    
    path('', views.home, name='home'),

]
