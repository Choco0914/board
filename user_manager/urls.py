from django.urls import path, re_path, include
from . import views

app_name = 'user_manager'

urlpatterns = [
        # login
        re_path(r'^login/$', views.login, name='login'),

        # validate
        re_path(r'^login/validate/$', views.login_validate, name='login_validate'),
]
