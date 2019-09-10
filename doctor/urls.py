from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (DoctorList ,BookingList, 
				   CommentList,CreateBooking,
				   AppointmentAPI,
				   AppointmentView,
				   AttendenceView,
				   PaymentView)
from rest_framework import routers
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet

app_name = 'doctor'

router = routers.DefaultRouter()
router.register('doctors-list', DoctorList)
router.register('bookings-list', BookingList)
router.register('comments-list', CommentList)
router.register('appointment', AppointmentView)
router.register('devices', FCMDeviceAuthorizedViewSet)
router.register('attendence',AttendenceView)
router.register('payment',PaymentView)
urlpatterns = [
	path('', include(router.urls)),
	path('appointment/',AppointmentAPI.as_view(), name='appointments'),
	path('bookings/',CreateBooking.as_view(),name='bookingss'),
	# path('push/', push_notifications,name='pushnoti'),
	# path('doctors/', DoctorList.as_view({'get': 'list'}), name ='doctors-list'),
	# path('clients/', ClientList.as_view(), name ='clients-list'),
	# path('bookings/', BookingList.as_view(), name ='booking-list'),
	# path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	]

# urlpatterns = format_suffix_patterns(urlpatterns)