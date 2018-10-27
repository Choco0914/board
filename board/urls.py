from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # board application
    re_path(r'', include('post_service.urls')),

    # user_manager
    re_path(r'^user/', include('user_manager.urls')),
]
