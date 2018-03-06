from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = 'HMSApp'
urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^room_allotment/$', login_required(views.RoomAllotmentView.as_view()), name='room_allotment'),
    url(r'^profile/$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^complaints/$', login_required(views.HostelComplaintsView.as_view()), name='complaints'),
    url(r'^applications/$', login_required(views.AllApplicationsView.as_view()), name='all_applications'),
    url(r'^applications/(?P<req_id>\d+)/$$', login_required(views.AllApplicationsView.as_view()), name='all_applications'),
    url(r'^notice_board/$', login_required(views.NoticeBoardView.as_view()), name='notice_board'),
    url(r'^all_complaints/$', login_required(views.AllComplaintsView.as_view()), name='all_complaints'),
    url(r'^all_complaints/(?P<req_id>\d+)/$$', login_required(views.AllComplaintsView.as_view()), name='all_complaints'),
    url(r'^room_allotment_letter/$', login_required(views.DownloadRoomAllotmentView.as_view()), name='download'),
]	