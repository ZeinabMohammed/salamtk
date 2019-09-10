from django.urls import path,include
from rest_framework import routers
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from .views import NotificationView

app_name='notification'


router=routers.DefaultRouter()
router.register('notification',NotificationView)
# router.register('commentnoti',CommentDoctorView)
urlpatterns = [
	path('', include(router.urls)),


	]