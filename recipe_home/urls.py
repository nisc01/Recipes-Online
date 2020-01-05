from . import views
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView


urlpatterns = [
    path(r'', views.home, name = 'home'),
    path(r'sign_in',views.sign_in, name='sign_in'),
    path(r'sign_up',views.sign_up, name='sign_up'),
    path(r'add_user',views.add_user,name='add_user'),
    path(r'user_authenticate',views.user_authenticate,name='user_authenticate'),
    path(r'log_out',views.log_out,name='log_out'),
]
