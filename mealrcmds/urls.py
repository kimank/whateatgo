from django.conf.urls import url
from . import views
app_name = 'mealrcmds'
urlpatterns = [
    url(r'^$', views.index),
]