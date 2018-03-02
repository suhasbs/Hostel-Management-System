from django.conf.urls import url
from . import views

app_name = 'HMSApp'
urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^room_allotment/$', views.RoomAllotmentView.as_view(), name='room_allotment'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^complaints/$', views.HostelComplaintsView.as_view(), name='complaints'),
    url(r'^applications/$', views.AllApplicationsView.as_view(), name='all_applications'),
    url(r'^applications/(?P<req_id>\d+)/$$', views.AllApplicationsView.as_view(), name='all_applications'),
]