
from django.conf.urls import url
from . import views


def test(request, id):
    print """
    
    $$$$$$$$$$$
    **    *****
    
    
    """
urlpatterns = [
    
    url(r'^dashboard$', views.dashboard),
    url(r'^addtrip$', views.addtrip),
    url(r'^createtrip$', views.createtrip),
    url(r'^joinTrip/(?P<id>\d+)$', views.jointrip),
    url(r'^logout$', views.logout),
    url(r'^show/(?P<id>\d+)$', views.show),
   
]
