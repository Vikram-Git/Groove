from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name="register"),
    url(r'^edit-profile/$', views.edit_profile, name="edit-profile"),
    url(r'^edit-picture/$', views.edit_picture, name="edit-picture"),
    url(r'^edit-password/$', views.edit_password, name='edit-password'),

    url(r'^about-groove/$', views.about_groove, name='about-groove'),
]

