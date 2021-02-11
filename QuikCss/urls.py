from django.urls import path

from QuikCss.views import *

urlpatterns = [
    path('', home, name="home"),
]
