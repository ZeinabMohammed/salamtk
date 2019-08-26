from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DoctorList ,BookingList, CommentList
from rest_framework import routers

app_name = 'doctor'

router = routers.DefaultRouter()
router.register('doctors-list', DoctorList)
router.register('bookings-list', BookingList)
router.register('comments-list', CommentList)


urlpatterns = [
	path('', include(router.urls)),
	
	# path('doctors/', DoctorList.as_view({'get': 'list'}), name ='doctors-list'),
	# path('clients/', ClientList.as_view(), name ='clients-list'),
	# path('bookings/', BookingList.as_view(), name ='booking-list'),
	# path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	]

# urlpatterns = format_suffix_patterns(urlpatterns)