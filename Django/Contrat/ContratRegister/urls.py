from django.conf.urls import url
from . import views


urlpatterns = [
    url('register/$', views.register,name='register'),
    url('register_form/$', views.register_form, name='register_form'),
    url('log_in_page/$', views.log_in_page, name='log_in_page'),
]

