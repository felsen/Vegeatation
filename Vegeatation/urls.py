from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = patterns(

    '',

    url(
        r'^admin/',
        include(admin.site.urls)
        ),

    url(
        r'^',
        include('Profiles.urls')
        ),

    url(
        r'^user-login/$',
        auth_views.login,
        {'template_name': 'user_login.html'},
        name='user-login'
        ),

    url(
        r'^logout/$',
        auth_views.logout,
        {'next_page': 'user-login'},
        name='user-logout'
        ),

)
