from __future__ import absolute_import

from django.conf.urls import url, include
from django.views.generic.list import ListView

from .models import get_active_members


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=get_active_members(), template_name='members/member_list.html')),

    url('', include('django.contrib.auth.urls')),

    url(r'^valid_user/?$', 'members.views.valid_user',),
    url(r'^history/$',     'members.views.members_history'),
    url(r'^collection/$',  'members.views.members_bankcollection_list'),
    url(r'^keylist/$',     'members.views.members_key_list'),
    url(r'^lazzzorlist/$', 'members.views.members_lazzzor_list'),

    url(r'^(?P<user_username>(\w|-)+)/update/userpic/$',              'members.views.members_update_userpic', {}, 'update_member_avatar'),
    url(r'^(?P<user_username>(\w|-)+)/update/(?P<update_type>\w+)/$', 'members.views.members_update', {}, 'update_member_details'),
    url(r'^(?P<user_username>(\w|-)+)/$',                             'members.views.members_details', {}, 'show_member_details'),
]
