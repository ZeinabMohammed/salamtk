from django.shortcuts import render

from django.shortcuts import render
from .models import *
from .serializers import DoctorSerializer, CommentSerializer,BookingSerializer
from rest_framework.reverse import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework import permissions,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters

from . import paginations
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# API views

class DoctorList(viewsets.ModelViewSet):
	# permission_classes  = (permissions.IsAuthenticatedOrReadOnly,)
	queryset 			= Doctor.objects.all()
	serializer_class	= DoctorSerializer
	pagination_class  	=[paginations.DoctorListPagination]
	filter_backends 	= [DjangoFilterBackend, SearchFilter]
	filterset_fields    = ['name','specialization','clinic_address','country']
	search_fields 	    = ['name','specialization', 'country']
	ordering            = ['name']
class BookingList(viewsets.ModelViewSet):
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset		   = Booking.objects.all()
	serializer_class   = BookingSerializer
	pagination_class   = [paginations.BookingListPagination]
	filter_backends	   = [DjangoFilterBackend, SearchFilter,OrderingFilter]
	filterset_fields   = ['doctor','user',]
	search_fields 	   = ['doctor', 'user']
	ordering   		   = ['-checkup_date']

class CommentList(viewsets.ModelViewSet):
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset		   = Comment.objects.all()
	serializer_class   = CommentSerializer
	pagination_class  	=[paginations.CommentListPagination]
	filter_backends    = [DjangoFilterBackend, SearchFilter,OrderingFilter]
	filterset_fields   = ['doctor','user',]
	search_fields 	   = ['__all__']
	ordering           = ['-date_posted']

#create endpoint for root of API:	
# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticatedOrReadOnly,])
# def api_root(request, format=None):
# 	return Response({
# 					 'doctors': reverse('users:doctors-list', request=request, format=format),
# 					 'clients':reverse("users:clients-list", request=request, format=format),
# 					 'bookings':reverse("users:booking-list", request=request, format=format)
# 					})