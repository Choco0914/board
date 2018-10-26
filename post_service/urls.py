""" post_service url 패턴 정의 """
from django.urls import path, re_path, include
from . import views

app_name = 'post_service'

urlpatterns=[
    # list_home
    re_path(r'^$', views.post_list, name='list'),

    # login
    re_path(r'^login/$', views.login, name='login'),

    # validate
    re_path(r'^login/validate/$', views.login_validate, name='login_validate'),

]
