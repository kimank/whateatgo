from django.conf.urls import url
from . import views
app_name = 'mealrcmds'
urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^select', views.region),
    url(r'^result', views.select)
]