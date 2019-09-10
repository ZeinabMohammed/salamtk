from django.shortcuts import render

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView 
from rest_framework import permissions,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from fcm_django.models import FCMDevice
from notifications.utils import push_notifications
from . import paginations
from .models import *
from .serializers import (DoctorSerializer, 
						 CommentSerializer,
						 BookingSerializer,
						 AppointmentSerializer,
						 AttendanceSerializer,
						 PaymentSerializer)


# API views
class DoctorList(viewsets.ModelViewSet):
	# permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
	queryset 		 = Doctor.objects.all()
	serializer_class = DoctorSerializer
	pagination_class =paginations.DoctorListPagination
	filter_backends  = [DjangoFilterBackend, SearchFilter,]
	filterset_fields = '__all__'
	# search_fields 	    = ['name','specialization', 'country']
	# ordering            = ['name']
	
class BookingList(viewsets.ModelViewSet):
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset		 = Booking.objects.all()
	serializer_class = BookingSerializer
	pagination_class = paginations.BookingListPagination
	filter_backends	 = [DjangoFilterBackend, SearchFilter,OrderingFilter]
	filterset_fields = '__all__'
	search_fields 	 = ['doctor', 'user']
	ordering   		 = ['-appointment']

class CommentList(viewsets.ModelViewSet):
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset		   = Comment.objects.all()
	serializer_class   = CommentSerializer
	pagination_class   = paginations.CommentListPagination
	filter_backends    = [DjangoFilterBackend, SearchFilter,OrderingFilter,]
	filterset_fields   = '__all__'
	search_fields 	   = '__all__'
	ordering           = ['-date_posted']
	def create(self,request):
		serializer=CommentSerializer(data=request.data)
		if serializer.is_valid():
			# serializer.client = self.request.user
			serializer.save(user=request.user)
			push_notification(user,title,body)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateBooking(CreateAPIView):
	serializer_class   = BookingSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def post(self,request, format=None):
		# permission_classes = [IsOwnerOrReadOnly,]
		serializer = BookingSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user=request.user)
			# serializer.client = self.request.user
			push_notification(user, title, body)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AttendenceView(viewsets.ModelViewSet):
	queryset		 = Attendance.objects.all()
	serializer_class = AttendanceSerializer
	search_fields 	 = ['__all__']
class PaymentView(viewsets.ModelViewSet):
	queryset 		 = Payment.objects.all()
	serializer_class = PaymentSerializer
	search_fields    = ['__all__']
class AppointmentView(viewsets.ModelViewSet):
	queryset		 = Appointment.objects.all()
	serializer_class = AppointmentSerializer
	search_fields 	 = ['__all__']
    
class AppointmentAPI(APIView):
	"""RUD"""
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	def get_doctor(self,pk):
		try:
			return Doctor.objects.get(pk=pk)
		except Doctor.DoesNotExist:
			raise Http404
	
	def get(self, request,pk, format=None):
		doctor = self.get_doctor(pk)
		serializer = AppointmentSerializer(doctor,context={'request': request})
		return Response(serializer.data)
	def put(self, request,pk, format=None):
		doctor = self.get_doctor(pk)
		serializer = AppointmentSerializer(doctor, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
	def delete(self, request, pk, format=None):
		doctor = self.get_doctor(pk)
		doctor.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# from pyfcm import FCMNotification

# push_service = FCMNotification(api_key="<api-key>")
# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "title"
# message_body = "Dev loves Stack overflow"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)



#create endpoint for root of API:	
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly,])
# def api_root(request, format=None):
# 	return Response({
# 					 'doctors': reverse('users:doctors-list', request=request, format=format),
# 					 'clients':reverse("users:clients-list", request=request, format=format),
# 					 'bookings':reverse("users:booking-list", request=request, format=format)
# 					})