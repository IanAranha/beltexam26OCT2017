from django.conf.urls import url, include
from . import views

def test(request):
    print """
    
   YO YO YO YO
   
   
    """
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    
]
