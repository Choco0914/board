from django.urls import path, re_path, include
from . import views

app_name = 'user_manager'

urlpatterns = [
        # Join
        re_path(r'^join/$', views.join_page, name='join_page'),

        # login
        re_path(r'^login/$', views.login, name='login'),

        # validate
        re_path(r'^login/validate/$', views.login_validate, name='login_validate'),
]
