""" post_service url 패턴 정의 """
from django.urls import path, re_path, include
from . import views

app_name = 'post_service'

urlpatterns=[
    re_path(r'', views.post_list, name='list')
]
