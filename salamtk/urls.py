from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenVerifyView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('doctor.urls')),
    path('',include('notifications.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
